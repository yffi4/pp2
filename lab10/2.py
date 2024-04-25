import pygame
import time
import random
import psycopg2

# Подключение к базе данных
connection = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="15103016",
    port="5432"
)

cur = connection.cursor()

# Создание таблицы пользователей и счетов
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,
    current_level INT DEFAULT 1
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS user_score (
    username VARCHAR(255) PRIMARY KEY,
    score INT DEFAULT 0
);
""")
# Размер окна
window_x = 720
window_y = 480

# Границы
boundry = []

# Определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Определение уровней
levels = {
    1: {
        "speed": 15,
        "wall_color": pygame.Color(100, 100, 100),
        "walls": [
            (20, 0, window_x, 10),
            (30, 0, 10, window_y - 20),
            (window_x, window_y - 10, window_x, 5),
            (window_x - 20, 50, 250, window_y - 20)
        ]
    },
    2: {
        "speed": 20,
        "wall_color": pygame.Color(150, 75, 0),
        "walls": [
            (300, 150, window_x / 2, 100),
            (0, 100, 140, window_y - 203),
            (window_x - 170, 230, 10, window_y - 20),
            (340, window_y - 110, window_x / 2, 104)
        ]
    },
    3: {
        "speed": 25,
        "wall_color": pygame.Color(0, 100, 100),
        "walls": [
            (300, 15, window_x / 2, 100),
            (140, 100, 140, window_y - 203),
            (window_x - 70, 330, 10, window_y - 20),
            (240, window_y - 110, window_x / 2, 184)
        ]
    }
}


# Создание границ
def createWall():
    global boundry
    boundry = []
    for i in range(0, window_x):
        boundry.append((i, 0))
        boundry.append((i, window_y - 18))
    for i in range(0, window_y):
        boundry.append((0, i))
        boundry.append((window_x - 18, i))


# Отрисовка границ
def drawWall():
    for each in boundry:
        wallRect = pygame.Rect(each[0], each[1], 10, 10)
        pygame.draw.rect(game_window, green, wallRect)


# Инициализация Pygame
pygame.init()

# Инициализация игрового окна
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS (кадры в секунду)
fps = pygame.time.Clock()

# Определение положения змеи по умолчанию
snake_position = [100, 50]

# Определение первых 4 блоков тела змеи
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# Позиция фрукта
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# Направление змеи по умолчанию
direction = 'RIGHT'
change_to = direction

# Начальная оценка
score = 0

# Таймер для появления фрукта
fruit_timer = 0


# Отображение функции Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# Функция завершения игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    update_user_score(user)
    pygame.quit()
    quit()


# Функция для вставки нового пользователя в базу данных
def insert_new_user(new_user):
    cur.execute("""INSERT INTO users VALUES ('{}', 1)""".format(new_user))
    cur.execute("""INSERT INTO user_score VALUES ('{}', 0)""".format(new_user))
    connection.commit()


# Функция для обновления счета пользователя в базе данных
def update_user_score(user_name):
    cur.execute("""UPDATE user_score
    SET score={}
    WHERE username='{}'
    """.format(score, user_name))
    connection.commit()


# Функция для получения текущего уровня пользователя
def get_user_level(user_name):
    cur.execute("SELECT current_level FROM users WHERE username='{}'".format(user_name))
    data = cur.fetchone()
    return data[0]


# Функция для установки текущего уровня пользователя
def set_user_level(user_name, level):
    cur.execute("""UPDATE users
    SET current_level={}
    WHERE username='{}'
    """.format(level, user_name))
    connection.commit()


# Функция для отрисовки стен
def draw_walls(level):
    for wall in levels[level]["walls"]:
        pygame.draw.rect(game_window, levels[level]["wall_color"], pygame.Rect(wall))


# Определение времени начала игры
start_time = time.time()

# Запрос имени пользователя
print("Enter your username:")
user = input()

# Ожидание ввода имени пользователя в течение 7 секунд
while time.time() - start_time < 7:
    pass

# Проверка существования пользователя в базе данных
cur.execute("SELECT count(*) FROM users WHERE username='{}'".format(user))
if cur.fetchone()[0] == 0:
    insert_new_user(user)
    print("New user {} has been created.".format(user))
else:
    print("Welcome back, {}!".format(user))
    print("Current level: {}".format(get_user_level(user)))

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                # При нажатии клавиши "p" игра приостанавливается
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            # При повторном нажатии "p" игра возобновляется
                            paused = False

    # Увеличение таймера для появления фрукта
    fruit_timer += 1

    # Если прошло более 7 секунд, сбросить фрукт
    if fruit_timer > 7 * levels[get_user_level(user)]["speed"]:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        fruit_timer = 0

    # Если две клавиши нажаты одновременно,
    # то выбирается только одно направление
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Перемещение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Механизм роста тела змеи и проверка поедания фрукта
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
        fruit_timer = 0  # Сбросить таймер при поедании фрукта
        update_user_score(user)
        # Проверка на достижение счета для перехода на следующий уровень
        if score >= 30:
            current_level = get_user_level(user)
            next_level = current_level + 1
            if next_level <= 3:  # Проверка, не достигнут ли последний уровень
                set_user_level(user, next_level)
                print(f"Congratulations! You've reached level {next_level}.")
                score = 0  # Сброс счета после перехода на новый уровень
            else:
                print("Congratulations! You've completed all levels.")
                game_over()
    else:
        snake_body.pop()

    # Если фрукт не съеден, то создаем новый
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        # Проверка, чтобы фрукт не появлялся внутри стен
        while fruit_position in boundry:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

    # Отрисовка змеи и фрукта на игровом поле
    game_window.fill(black)

    draw_walls(get_user_level(user))  # Отрисовка стен для текущего уровня
    drawWall()  # Отрисовка границ
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Условия завершения игры
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    for wall in levels[get_user_level(user)]["walls"]:
        wall_rect = pygame.Rect(wall)
    if wall_rect.colliderect(pygame.Rect(snake_position[0], snake_position[1], 10, 10)):
        game_over()

    # Отображение счета
    show_score(1, white, 'times new roman', 20)

    # Обновление игрового экрана
    pygame.display.update()

    # Ограничение FPS
    fps.tick(levels[get_user_level(user)]["speed"])
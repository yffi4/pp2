import time

import pygame
import random


pygame.init() # Инициализация Pygame

#Размер экрана
WIDTH = 600
HEIGHT = 600

#размер клетки поля
CELL = 30
#цветовая палитра
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

#Функция для отрисовки сетки
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess(): # Функция для отрисовки шахматной доски
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))  # Создание игрового окна

class Point: # Класс для представления точек на игровом поле
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake: # Класс для змеи
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  #Начальное направление движения по оси X
        self.dy = 0  #Начальное направление движения по оси Y
        self.score = 0 #Счет игрока
        self.level = 1 #Уровень игры
        self.foods_eaten = 0 #Количество съеденной еды
        self.speed = 5 #Скорость змеи


    def move(self):  #Функция для движения змеи
        for i in range(len(self.body) - 1, 0, -1): #Перемещаем каждый сегмент змеи на следующий
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx  #Перемещаем голову змеи в соответствии с направлением
        self.body[0].y += self.dy

        #Проверяем столкновение с границами игрового поля
        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            return True
        #Проверяем столкновение змеи с самой собой
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                return True
        return False
    def draw(self): #Функция для отрисовки змеи
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food): #Функция для проверки столкновения с едой
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y: #Если голова змеи находится на месте еды
            print("Got food!")
            self.body.append(Point(head.x, head.y)) #Добавляем сегмент к телу змеи
            self.foods_eaten += 1 #Увеличиваем счетчик съеденной еды
            self.score += random.randint(5, 20) #Увеличиваем счет игрока
            if self.foods_eaten % 3 == 0: #Проверяем, съедена ли определенное количество еды
                self.level += 1 #Увеличиваем уровень
                self.speed += 1 #Увеличиваем скорость змеи
            return True
        return False
class Food: #Класс для еды
    def __init__(self, snake):
        self.pos = self.generate_food_position(snake) #Генерируем случайную позицию для еды
        self.last_touch_pos = time.time()
        self.moved = False
    def reset_timer(self):
        self.last_touch_time = time.time()  # Сбрасываем таймер времени без касания
        self.moved = False

    def generate_food_position(self, snake): #Функция для генерации позиции еды
        available_positions = [Point(x, y) for x in range(WIDTH // CELL) for y in range(HEIGHT // CELL) if Point(x, y) not in snake.body]
        return random.choice(available_positions)  #Выбираем случайную позицию из доступных

    def update_position(self, snake):
        self.pos = self.generate_food_position(snake)  # Обновляем позицию еды
        self.reset_timer()  # Сбрасываем таймер
    def draw(self): #Функция для отрисовки еды
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)) #Отрисовка квадрата еды

FPS = 5 #Частота кадров в секунду
clock = pygame.time.Clock() #Создание объекта Clock для управления временем

snake = Snake() #Создание объекта змеи
food = Food(snake)  #Создание объекта еды

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    draw_grid_chess() #Отрисовка игрового поля

    collision = snake.move() #Перемещение змеи и проверка столкновений

    if collision:
        print("Game over")
        break


    current_time = time.time()
    if not food.moved and current_time - food.last_touch_pos > 5:  # Если еда не перемещалась и прошло более 5 секунд
        food.update_position(snake)
        food.moved = True
    if snake.check_collision(food): #Проверка столкновения с едой
        food.moved = False
        food = Food(snake)  #Создание новой еды
    screen.fill(colorBLACK) #Устанавливает цвет поля

    snake.draw()#Отрисовка змеи
    food.draw() #Отрисовка еды

    #Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake.score}", True, colorWHITE)
    level_text = font.render(f"Level: {snake.level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip() #Обновление экрана
    clock.tick(snake.speed) #Ограничение частоты кадров

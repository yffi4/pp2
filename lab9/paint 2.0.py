import pygame
pygame.init()

# Определение переменных
fps = 60  # Количество кадров в секунду
timer = pygame.time.Clock()  # Таймер для управления FPS
WIDTH = 800  # Ширина экрана
HEIGHT = 600  # Высота экрана
active_figure = 0  # Тип активной фигуры (0 - круг, 1 - прямоугольник, и т.д.)
active_color = (255, 255, 255)  # Текущий цвет для рисования

# Создание графического окна
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []  # Список для хранения нарисованных фигур

# Переменные для динамического рисования
is_drawing = False  # Флаг для определения, идет ли в данный момент рисование
start_pos = None  # Начальная позиция рисования
current_shape = None  # Временно хранит фигуру, которую рисуют в данный момент

# Константы для типов фигур
CIRCLE = 0
RECTANGLE = 1
SQUARE = 2
RECTANGLE_TRIANGLE = 3
EQUILATERAL_TRIANGLE = 4
RHOMBUS = 5
ERASER = 6  # Добавляем константу для ластика

def draw_menu(color):
    # Отрисовка меню для выбора фигур и цветов
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])  # Серый фон верхней панели
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)  # Черная линия под верхней панелью

    # Рисование иконок для выбора кистей
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]  # Круглая кисть
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)

    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]  # Прямоугольная кисть
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20],2)

    square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), SQUARE]  # Квадратная кисть
    pygame.draw.rect(screen, 'white', [135, 15, 40, 40],2)

    rect_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), RECTANGLE_TRIANGLE]  # Кисть для прямоугольного треугольника
    pygame.draw.polygon(screen, 'white', [(230, 20), (230, 50), (196, 50)],2)

    equi_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), EQUILATERAL_TRIANGLE]  # Кисть для равнобедренного треугольника
    pygame.draw.polygon(screen, 'white', [(252, 20), (300, 20), (275, 55)],2)

    rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), RHOMBUS]  # Кисть для ромба
    pygame.draw.polygon(screen, 'white', [(335, 20), (360, 35), (335, 50), (310, 35)],2)

    # Загрузка и отрисовка иконки ластика
    eraser = pygame.image.load("media/eraser-square-svgrepo-com.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 50  # Увеличиваем размер ластика
    screen.blit(eraser, [WIDTH - 150, 7, 50, 50])

    # Формируем список кистей
    brush_list = [circle_brush, rect_brush, square_brush, rect_triangle_brush, equi_triangle_brush, rhombus_brush]

    # Отрисовка текущего выбранного цвета
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Отрисовка кнопок выбора цвета
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])

    color_rect = [blue, red, green, yellow, teal, purple, black, white]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255

, 255, 255)]

    return brush_list, color_rect, rgb_list, eraser_rect  # Возвращаем eraser_rect

def draw_painting(paints):
    # Отрисовка всех нарисованных фигур на холсте
    for color, start_pos, figure, end_pos in paints:
        if figure == CIRCLE:  # Круг
            radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, color, start_pos, radius, 2)
        elif figure == RECTANGLE:  # Прямоугольник
            pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])),2)
        elif figure == SQUARE:  # Квадрат
            width = end_pos[0] - start_pos[0]
            height = end_pos[1] - start_pos[1]
            size = min(abs(width), abs(height))
            if width < 0:
                start_pos = (start_pos[0] - size, start_pos[1])
            if height < 0:
                start_pos = (start_pos[0], start_pos[1] - size)
            pygame.draw.rect(screen, color, (start_pos, (size, size)),2)
        elif figure == RECTANGLE_TRIANGLE:  # Прямоугольный треугольник
            pygame.draw.polygon(screen, color, [(start_pos[0], end_pos[1]), end_pos, start_pos],2)
        elif figure == EQUILATERAL_TRIANGLE:  # Равнобедренный треугольник
            triangle_height = abs(end_pos[1] - start_pos[1])  # Высота равнобедренного треугольника
            half_base = abs(end_pos[0] - start_pos[0]) / 2  # Половина основания равнобедренного треугольника
            top_point = (start_pos[0], start_pos[1] - triangle_height)  # Верхняя вершина
            left_point = (start_pos[0] - half_base, start_pos[1])  # Левая вершина
            right_point = (start_pos[0] + half_base, start_pos[1])  # Правая вершина
            pygame.draw.polygon(screen, color, [top_point, left_point, right_point],2)
        elif figure == RHOMBUS:  # Ромб
            center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
            pygame.draw.polygon(screen, color,
                                [(center[0], start_pos[1]), (end_pos[0], center[1]), (center[0], end_pos[1]),
                                 (start_pos[0], center[1])],2)
        elif figure == ERASER:  # Ластик
            # Рисуем белый прямоугольник следом за курсором
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(end_pos, (50, 50)))

# Основной цикл программы
done = False
while not done:
    timer.tick(fps)  # Ограничиваем частоту кадров
    screen.fill("white")  # Заливаем экран белым цветом
    mouse = pygame.mouse.get_pos()  # Получаем текущие координаты мыши
    left_click = pygame.mouse.get_pressed()[0]  # Получаем состояние левой кнопки мыши

    # Рисуем меню и получаем список кистей, цветов и прямоугольника ластика
    brushes, colors, rgbs, eraser_rect = draw_menu(active_color)

    # Проверяем нажатие и отпускание левой кнопки мыши для начала и завершения рисования
    if left_click and mouse[1] > 70 and not is_drawing:
        is_drawing = True
        start_pos = mouse
        current_shape = [active_color, start_pos, active_figure, start_pos]  # Инициализация текущей фигуры

    if not left_click and is_drawing:
        painting.append(current_shape)
        is_drawing = False

    # Если идет рисование, обновляем текущую фигуру
    if is_drawing:
        current_shape[-1] = mouse

    # Отрисовываем все фигуры на холсте
    draw_painting(painting)

    # Отрисовываем текущую фигуру (если есть)
    if current_shape:
        draw_painting([current_shape])

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN and mouse[1] <= 70:
            # Обработка выбора цвета или кисти
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for brush in brushes:
                if brush[0].collidepoint(event.pos):
                    active_figure = brush[1]

        if event.type == pygame.MOUSEBUTTONDOWN and eraser_rect.collidepoint(event.pos):
            # Обработка выбора ластика
            active_color = (255, 255, 255)  # Устанавливаем белый цвет
            active_figure = ERASER

    pygame.display.flip()  # Обновление экрана

pygame.quit()  # Завершение работы приложения

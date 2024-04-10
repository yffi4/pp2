import  pygame
pygame.init()


fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = (255, 255, 255)  # Use a tuple for color

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []

# New variables for dynamic drawing
is_drawing = False
start_pos = None
current_shape = None  # Temporarily stores the shape being drawn

def draw_menu(color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    brush_list = [circle_brush, rect_brush]

    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Load eraser icon here if necessary or replace with a pygame.draw call for simplicity
    # pygame.draw.rect(screen, 'white', [WIDTH - 150, 7, 25, 25])  # Placeholder for eraser icon

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
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for color, start_pos, figure, end_pos in paints:
        if figure == 0:  # Circle
            radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, color, start_pos, radius, 2)
        elif figure == 1:  # Rectangle
            pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)

run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu(active_color)

    if left_click and mouse[1] > 70 and not is_drawing:
        # Start drawing
        is_drawing = True
        start_pos = mouse
        current_shape = [active_color, start_pos, active_figure, start_pos]  # Initialize current_shape

    if not left_click and is_drawing:
        # Finalize drawing
        painting.append(current_shape)
        is_drawing = False

    if is_drawing:
        # Update current drawing
        current_shape[-1] = mouse

    draw_painting(painting)

    # Draw the current shape being drawn
    if current_shape:
        draw_painting([current_shape])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and mouse[1] <= 70:
            # Select color or brush
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

    pygame.display.flip()

pygame.quit()
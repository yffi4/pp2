import pygame as pg, datetime
pg.init()
screen = pg.display.set_mode((800, 700))
clock = pg.time.Clock()
done = False


clock_face = pg.image.load('pictures/mickey.png')
left_hand = pg.image.load('pictures/left.png')
right_hand = pg.image.load('pictures/right.png')

clock_face_rect = clock_face.get_rect(center=(400, 350))
left_hand_rect = left_hand.get_rect(center=clock_face_rect.center)
right_hand_rect = right_hand.get_rect(center=clock_face_rect.center)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    current_time = datetime.datetime.now().time()
    seconds_angle = current_time.second * 6
    minutes_angle = (current_time.minute * 60 + current_time.second) / 50

    rotated_left_hand = pg.transform.rotate(left_hand, -seconds_angle)
    rotated_right_hand = pg.transform.rotate(right_hand, -minutes_angle)

    left_hand_rect = rotated_left_hand.get_rect(center=clock_face_rect.center)
    right_hand_rect = rotated_right_hand.get_rect(center=clock_face_rect.center)

    screen.blit(clock_face, clock_face_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    screen.blit(rotated_right_hand, right_hand_rect)

    pg.display.flip()

    clock.tick(60)


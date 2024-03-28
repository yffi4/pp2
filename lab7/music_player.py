import pygame as pg

pg.init()
done = False
screen = pg.display.set_mode((320, 320))
background = pg.image.load('pictures/i.png')
background_rect = background.get_rect()
songs = ['tracks/_Kanye_West_Ty_Dolla_ign_-_CARNIVAL_77458919.mp3',
         'tracks/21_Savage_-_redrum_77271533.mp3',
         'tracks/The_Weeknd_-_Save_Your_Tears_68852989.mp3',]

true_song = 0   
pg.mixer.music.load(songs[true_song])
pg.mixer.music.play()

music_playing = True
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if music_playing:
                    pg.mixer.music.pause()
                    music_playing = False
                else:
                    pg.mixer.music.unpause()
                    music_playing = True
            elif event.key == pg.K_RIGHT:
                true_song += 1
                if true_song >= len(songs):
                    true_song = 0
                pg.mixer.music.load(songs[true_song])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                true_song -= 1
                if true_song < 0:
                    true_song = len(songs) - 1
                pg.mixer.music.load(songs[true_song])
                pg.mixer.music.play()
    screen.blit(background, background_rect)
    pg.display.flip()

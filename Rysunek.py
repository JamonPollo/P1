import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((1000, 800))


running = True

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
LIGHTERYELLOW = (255,255,102)
YELLOW = (255,255,0)
GREEN = (0,255,0)
LIGHTBLUE = (204,255,229)
OCEANBLUE = (102,178,255)
BROWN = (153,76,0)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pg.draw.rect(screen,LIGHTERYELLOW,pg.Rect(0,500,1000,800))
    pg.draw.rect(screen,OCEANBLUE,pg.Rect(0,470,1000,130))
    pg.draw.circle(screen,LIGHTBLUE,(50,20),50)
    pg.draw.circle(screen,LIGHTBLUE,(120,20),50)
    pg.draw.circle(screen,LIGHTBLUE,(200,20),50)
    pg.draw.circle(screen,LIGHTBLUE,(400,30),50)
    pg.draw.circle(screen,LIGHTBLUE,(480,30),50)
    pg.draw.circle(screen,LIGHTBLUE,(550,30),50)
    pg.draw.circle(screen,YELLOW,(990,30),90)

    pg.draw.rect(screen,BLACK,pg.Rect(200,700,10,80))
    POINTS = [(140,700),(260,700),(200,650)]
    pg.draw.polygon(screen,RED,POINTS)

    pg.draw.line(screen,BROWN,(350,750),(450,750),7)
    pg.draw.line(screen,BROWN,(445,750),(500,700),7)

    pg.display.flip()

pg.quit()
import pygame as pg
import sys
from os import path
pg.init()
vec = pg.math.Vector2

a = vec(1,1)
b = vec(2,2)


game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'IMG')
player_img = pg.image.load(path.join(img_folder, "starship.BMP"))
player_img.set_colorkey((0,119,64))
direction = vec(1,0)

pos = vec(600,300)
pos2 = (0,0)
speed = 0.00
angle = 0
angle2 =0





    
    




while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        direction.rotate_ip(-0.2)
        angle -=0.2
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        direction.rotate_ip(0.2)
        angle += 0.2
    if keys[pg.K_UP] or keys[pg.K_w]:
        speed += 0.002
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        speed -= 0.002

    
    screen.fill(black)
    img = pg.Surface((100,5))
    #img = img.fill((255,0,0))
    screen.blit(img,(10,10))
    
    player_img2 = pg.transform.rotate(player_img, -angle)
    rect = player_img2.get_rect()
    rect.center = (pos.x, pos.y)
    screen.blit(player_img2,rect)
    pg.draw.line(screen,(255,0,0),pos,pos+direction*speed*20)
    pos = pos+direction*speed
    
    pg.display.flip()

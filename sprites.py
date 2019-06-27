import pygame as pg
from settings import *
import random

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, img, animation, key_set):
        #game link
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #movement
        self.pos = vec(x,y)
        self.dir = vec(1,0)
        self.img = img
        self.img_b = img
        self.ang = 0
        self.speed = 0
        self.rect = self.img.get_rect()
        #animation
        self.ani = animation
        self.ani_b = self.ani
        self.ani_vis = False
        self.animate = Animate(self.game,self)
        #keys
        self.key_set = key_set
        #stats
        self.fuel = 100
        self.health = 100

    def get_keys(self):
        keys = pg.key.get_pressed();
        a = self.game.dt * 300
        b = a/100
        
        if keys[self.key_set[0]] :
            self.dir.rotate_ip(-a)
            self.ang -= a         
        if keys[self.key_set[1]]:
            self.dir.rotate_ip(a)
            self.ang += a
        if keys[self.key_set[2]] :
            self.speed += b
            self.fuel -= 0.2
            self.ani_vis = True
        if keys[self.key_set[3]]:
            self.speed -= b
        if keys[self.key_set[4]]:
            self.speed -= b
        if keys[self.key_set[5]]:
            self.speed -= b

        


    def update(self):
        
            self.ani_vis = False
            self.get_keys();
            self.img = pg.transform.rotate(self.img_b, -self.ang)
            self.ani = pg.transform.rotate(self.ani_b, -self.ang)
            self.rect = self.img.get_rect()
            self.rect.center = (self.pos.x, self.pos.y)
            self.pos = self.pos+( self.dir * self.speed)
            if(is_out_of_bounds(self.game,self)):
                self.health -= 1
            pg.draw.line(self.game.screen,(255,0,0),self.pos,self.pos+self.dir*self.speed*20)


class Animate(pg.sprite.Sprite):
    def __init__(self, game, player):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player = player
        self.img = self.player.ani
        self.rect = self.player.rect
        self.vis = self.player.ani_vis
        self.pos = vec(-10,-10)


    def update(self):
        self.vis = self.player.ani_vis
        if (self.vis):
            self.img = self.player.ani
            self.rect = self.player.rect
        else:
            self.rect.center = (-10,-10)

class Bars(pg.sprite.Sprite):
    def __init__(self,game,x,y,health,fuel,player):
        self.groups = game.drawable
        pg.sprite.Sprite.__init__(self, self.groups)
        self.player = player
        self.pos = vec(x,y)
        self.health = health
        self.fuel = fuel
        self.health_color = (0,255,0)
        self.fuel_color = (0,0,255)
        self.fuel_bar = ((self.pos.x,self.pos.y), (self.fuel , 5 )  )
        self.health_bar = ((self.pos.x,self.pos.y+10), (self.health , 5 )  )
        
        


        
    def update(self):
        
        self.fuel_bar = ((self.pos.x,self.pos.y), (number_cap(0,       self.fuel,          self.player.fuel) , 5 )  )
        self.health_bar = ((self.pos.x,self.pos.y+10), (number_cap(0,   self.health,  self.player.health) , 5 )  )

class Supplies(pg.sprite.Sprite):
    def __init__(self,game,img):
        self.game = game
        self.groups = game.stuff
        pg.sprite.Sprite.__init__(self, self.groups)
        self.img =img
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(1,1199),random.randint(1,599))

    def update(self):
        for sprites in self.game.all_sprites:
            if(self.rect.collidepoint(sprites.pos.x,sprites.pos.y)):
                sprites.fuel += 10
                self.rect.center = (random.randint(1,1199),random.randint(1,599))
                



def is_out_of_bounds(game,sprite):
    if(sprite.pos.x < 0 or sprite.pos.x > game.width):
        return True
    if(sprite.pos.y < 0 or sprite.pos.y > game.height):
        return True
    else:
        return False

def number_cap(bottom, top, num):
    if(num>=top):
        return top
    if(num<=bottom):
        return bottom
    else:
        return num

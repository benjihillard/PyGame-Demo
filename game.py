import pygame as pg
import sys
from sprites import *
from settings import *
from os import path

class game:
    def __init__(self, width, height, title):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()

    def get_img(self,name):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'IMG')
        img = pg.image.load(path.join(img_folder, name))
        img.set_colorkey((0,119,64))
        return img
        


    def new(self):
        self.player_one =  self.get_img("starship.BMP")
        self.flames = self.get_img("flames.BMP")
        self.backround = self.get_img("space.JPG")
        self.health_img = self.get_img("health.BMP")
        self.fuel_img = self.get_img("fuel.BMP")
        self.all_sprites = pg.sprite.Group()
        self.drawable = pg.sprite.Group()
        self.stuff = pg.sprite.Group()
        self.player = Player(self,10,10,self.player_one,self.flames,PLAYER_ONE_KEY_SET)
        #self.player_2 = Player(self,40,40,self.player_one,self.flames,PLAYER_TWO_KEY_SET)
        self.bar = Bars(self,10,10,100,100,self.player)
        self.healh_box = Supplies(self,self.health_img)
        self.fuel_box = Supplies(self,self.fuel_img)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()

        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.drawable.update()
        self.stuff.update()
        return

    

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.backround,(0,0))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.img, sprite.rect)
        for sprite in self.stuff:
            self.screen.blit(sprite.img, sprite.rect)
        for sprite in self.drawable:
            pg.draw.rect(self.screen,sprite.health_color,sprite.health_bar)
            pg.draw.rect(self.screen,sprite.fuel_color,sprite.fuel_bar)
        pg.display.flip()
        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
        

    
        
g = game(1200,600,"fuel race")
while True:
    g.new()
    g.run()
    g.show_go_screen()

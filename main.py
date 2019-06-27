import pygame as pg
import sys
from game import *


g = game(1200,600,"fuel race")
while True:
    g.new()
    g.run()
    g.show_go_screen()

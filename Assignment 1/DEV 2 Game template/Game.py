import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 30
board_size = 10
car_texture = pygame.image.load("Content\car.png").convert()
entry_tile = build_square_matrix(board_size, offset)


def Update(cars):
    cars = map(cars, lambda i: i.Update())
    cars = filter(cars, lambda i: not i.IsArrived())

    return cars

def Draw(i):
    if i is not Empty:
        POSITION_X = i.Value.Position.Position.X
        POSITION_Y = i.Value.Position.Position.Y

        _width = int(offset / 3)
        screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                         (_width + POSITION_X * offset, 
                          _width + POSITION_Y * offset))
        Draw(i.Tail)

def Main():
    start = time.time()
    cars = Node(Car(entry_tile), Empty)
    step = 0

    while True:
        pygame.event.get()
        screen.fill(green)
        entry_tile.Reset()
        entry_tile.Draw(screen)

        #print(cars.length())

        cars = Update(cars)

        if step == 5:
            if not entry_tile.Taken:
                cars = Node(Car(entry_tile), cars)
                entry_tile.Taken = True
            
            step = 0

        step = step + 1

        Draw(cars)

        pygame.display.flip()
        #time.sleep(1)
    
Main()
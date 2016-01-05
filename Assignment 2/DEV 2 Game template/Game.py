import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *
from Boat import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10
entry_road, entry_rivers, bridges = build_scene(size, offset)

#faces to the right
boat_texture = pygame.image.load("Content/tanker.png").convert_alpha()

#faces to the right
car_texture = pygame.image.load("Content/car.png").convert_alpha()

def Main():
    start = time.time()

    # Initial vars
    cars = Node(Car(entry_road.Value, False, car_texture), Empty)
    boats = Node(Boat(entry_rivers.Value, False, boat_texture), Empty)
    step = 0

    while True:
        pygame.event.get()
        screen.fill(green)

        # Draw board
        _board = entry_road
        while not _board.IsEmpty:
            _board.Value.Draw(screen, False)
            _board = _board.Tail

        # Draw bridges
        _board = bridges
        while not _board.IsEmpty:
            _board.Value.Draw(screen, True)
            _board = _board.Tail

        # Update and filter
        cars = cars.map(lambda i: i.Update()).filter(lambda i: not i.CanRemove)
        boats = boats.map(lambda i: i.Update()).filter(lambda i: not i.CanRemove)

        # Spawn every 5 frames
        if step == 5:
            if not entry_road.Value.Taken:
                cars = Node(Car(entry_road.Value, False, car_texture), cars)

            if not entry_rivers.Value.Taken:
                boats = Node(Boat(entry_rivers.Value, False, boat_texture), boats)

            step = 0
        step = step + 1

        # Draw
        cars.map(lambda i: i.Draw(screen, offset))
        boats.map(lambda i: i.Draw(screen, offset))

        pygame.display.flip()
        time.sleep(1) #0.2
    
Main()
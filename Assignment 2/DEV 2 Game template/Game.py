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
    entities = Empty

    # Start at 5 so entities will spawn on first frame
    step = 5

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

        # Update and filter entities
        entities = entities.filter(lambda i: not i.CanRemove()).map(lambda i: i.Update())

        # Spawn every 5 frames
        if step == 5:
            if not entry_road.Value.Taken:
                entities = Node(Car(entry_road.Value, False, car_texture), entities)
                entry_road.Value.Taken = True

            if not entry_rivers.Value.Taken:
                entities = Node(Boat(entry_rivers.Value, False, boat_texture), entities)
                entry_rivers.Value.Taken = True

            step = 0
        step = step + 1

        # Draw/update entities on the screen
        entities.map(lambda i: i.Draw(screen, offset))

        pygame.display.flip()
        time.sleep(0.2)
    
Main()
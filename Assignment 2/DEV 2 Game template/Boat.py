import random
from Node import *
from Common import *

class Boat:
    def __init__(self, position, canRemove, texture):
        self.Position = position
        self.CanRemove = canRemove
        self.Texture = texture

    def Update(self):
        directions = Empty
        position = self.Position
        
        if Boat.IsTraverseable(position.Up):
            directions = Node(position.Up, directions)

        if Boat.IsTraverseable(position.Down):
            directions = Node(position.Down, directions)

        if Boat.IsTraverseable(position.Left):
            directions = Node(position.Left, directions)

        if Boat.IsTraverseable(position.Right):
            directions = Node(position.Right, directions)

        # Do we have somewhere to go to?
        if directions is not Empty:
            position.Taken = False
            
            if position.Harbor:
                self.CanRemove = True
                position.Taken = False
            else:
                position = directions.random().Value
                position.Taken = True

            return Boat(position, self.CanRemove, self.Texture)

        # Stay stationary if there is nowhere to go
        return Boat(self.Position, self.CanRemove, self.Texture)

    def Draw(self, screen, offset):
        POSITION_X = self.Position.Position.X
        POSITION_Y = self.Position.Position.Y

        _width = int(offset / 3)
        screen.blit(pygame.transform.scale(self.Texture, (_width, _width)), 
                            (_width + POSITION_X * offset, 
                            _width + POSITION_Y * offset))

    def IsTraverseable(tile):
        if tile and tile != None and not tile.Taken:
            if not tile.River and tile.Harbor or tile.River:
                return True

        return False

import random
from Node import *
from Common import *

class Car:
    def __init__(self, position, canRemove, texture, prevPosition = Empty):
        self.Position = position
        self.PrevPosition = prevPosition
        self.CanRemove = canRemove
        self.Texture = texture

    def Update(self):
        directions = Empty
        position = prevPosition = self.Position
        
        if Car.IsTraverseable(position.Up):
            directions = Node(position.Up, directions)

        if Car.IsTraverseable(position.Down):
            directions = Node(position.Down, directions)

        if Car.IsTraverseable(position.Left):
            directions = Node(position.Left, directions)

        if Car.IsTraverseable(position.Right):
            directions = Node(position.Right, directions)

        # Do we have somewhere to go to?
        if directions is not Empty:
            position.Taken = False
            
            if position.Park:
                self.CanRemove = True
                position.Taken = False
            else:
                position = directions.random().Value
                position.Taken = True

            return Car(position, self.CanRemove, self.Texture, prevPosition)

        # Stay stationary if there is nowhere to go
        return Car(self.Position, self.CanRemove, self.Texture, self.PrevPosition)

    def Draw(self, screen, offset):
        POSITION_X = self.Position.Position.X
        POSITION_Y = self.Position.Position.Y

        # Rotate vehicle
        if self.PrevPosition != Empty:
            self.Texture = set_orientation(self.PrevPosition, self.Position, self.Texture)

        _width = int(offset / 3)
        screen.blit(pygame.transform.scale(self.Texture, (_width, _width)), 
                            (_width + POSITION_X * offset, 
                            _width + POSITION_Y * offset))

    def IsTraverseable(tile):
        if tile and tile != None and tile.Traverseable and not tile.Taken and not tile.Harbor:
             if not tile.River or tile.Bridge:
                return True
        
        return False

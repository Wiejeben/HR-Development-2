import random
from Node import *
from Common import *

class Vehicle():
    # Update entity
    def Update(self):
        directions = Empty
        position = prevPosition = self.Position
        
        # Check all posible directions
        if self.IsTraverseable(position.Up):
            directions = Node(position.Up, directions)

        if self.IsTraverseable(position.Down):
            directions = Node(position.Down, directions)

        if self.IsTraverseable(position.Left):
            directions = Node(position.Left, directions)

        if self.IsTraverseable(position.Right):
            directions = Node(position.Right, directions)

        # Do we have somewhere to go to?
        if directions is not Empty:
            position.Taken = False
            position = directions.random().Value
            position.Taken = True

            # Apply new position
            return self.__class__(position, self.CanRemove, self.Texture, prevPosition)

        # Stay stationary if there is nowhere to go
        return self.__class__(self.Position, self.CanRemove, self.Texture, self.PrevPosition)

    # Reposition entity
    def Draw(self, screen, offset):
        POSITION_X = self.Position.Position.X
        POSITION_Y = self.Position.Position.Y
        texture = self.Texture

        # Rotate entity
        if self.PrevPosition != Empty:
            texture = set_orientation(self.PrevPosition, self.Position, texture)

        # Reposition entity
        _width = int(offset / 3)
        screen.blit(pygame.transform.scale(texture, (_width, _width)), 
                            (_width + POSITION_X * offset, 
                            _width + POSITION_Y * offset))
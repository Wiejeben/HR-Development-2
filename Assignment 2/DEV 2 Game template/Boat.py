import random
from Node import *
from Common import *
from Vehicle import *

class Boat(Vehicle):
    def __init__(self, position, canRemove, texture, prevPosition = Empty):
        self.Position = position
        self.PrevPosition = prevPosition
        self.Texture = texture
    
    def CanRemove(self):
        position = self.Position

        # Check if vehicle can be removed
        if position.Harbor:
            position.Taken = False
            return True
        
        return False

    def IsTraverseable(self, tile):
        if tile and tile != None and not tile.Taken:
            if not tile.River and tile.Harbor or tile.River:
                return True

        return False

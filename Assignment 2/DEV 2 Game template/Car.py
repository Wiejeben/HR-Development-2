import random
from Node import *
from Common import *
from Vehicle import *

class Car(Vehicle):
    def __init__(self, position, canRemove, texture, prevPosition = Empty):
        self.Position = position
        self.PrevPosition = prevPosition
        self.Texture = texture
    
    def CanRemove(self):
        position = self.Position

        # Check if vehicle can be removed
        if position.Park:
            position.Taken = False
            return True
        
        return False

    def IsTraverseable(self, tile):
        # Check whether tile is allowed
        if tile and tile != None and tile.Traverseable and not tile.Taken and not tile.Harbor:
             if not tile.River or tile.Bridge:
                return True
        
        return False

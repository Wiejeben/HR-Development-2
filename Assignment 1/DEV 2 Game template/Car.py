import pygame
from Node import *

class Car:
    def __init__(self, position):
        self.Position = position

    def Update(self):
        directions = Empty
        position = self.Position
        
        # Check all possible directions
        if Car.IsTraverseable(position.Up):
            directions = Node(position.Up, directions)

        if Car.IsTraverseable(position.Down):
            directions = Node(position.Down, directions)

        if Car.IsTraverseable(position.Left):
            directions = Node(position.Left, directions)

        if Car.IsTraverseable(position.Right):
            directions = Node(position.Right, directions)

        if directions is not Empty:
            # Change tile status
            position.Taken = False
            position = directions.random().Value
            
            if not position.Park:
                position.Taken = True

            return Car(position)

        # Fallback if there is nowhere to go
        return Car(self.Position)

    # Check if tile can be moved to
    def IsTraverseable(position):
        return (position and position != None and position.Traverseable and not position.Taken)

    # Check if car is on parking spot
    def IsArrived(self):
        if self.Position.Park:
            return True
        
        return False
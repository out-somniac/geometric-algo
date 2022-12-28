from typing import Tuple, List
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Point():
    def __init__(self, x: float, y: float) -> 'Point':
        self.x = x
        self.y = y
    
    def __eq__(self, other) -> bool:
        return (self.x == other.x and self.y == other.y)
    
    def __str__(self) -> str:
        return "{}, {}".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def follows(self, other: 'Point') -> bool:
        return self.x > other.x and self.y > other.y
    
    def precedes(self, other: 'Point') -> bool:
        return self.x < other.x and self.y < other.y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        
class Rect():
    def __init__(self, lower_left: Tuple[float, float], upper_right: Tuple[float, float]) -> 'Rect':
        self.lower_left = Point(*lower_left)
        self.upper_right = Point(*upper_right) 
        
        if not self.lower_left.precedes(self.upper_right):
            raise ValueError('Lower-left point must precede the upper-right')
    
    def __eq__(self, other: 'Rect') -> bool:
        return self.lower_left == other.lower_left and self.upper_right == other.upper_right
    
    def __str__(self) -> str:
        return "{} - {}".format(self.lower_left, self.upper_right)
    
    def __repr__(self):
        return self.__str__()
    
    def intersects(self, other: 'Rect') -> bool:
        return self.lower_left.precedes(other.upper_right) and other.lower_left.precedes(self.upper_right)
    
    def contains_point(self, point: Point) -> bool: # Type of point is left intentionally ambiguous
        return self.lower_left.precedes(point) and self.upper_right.follows(point)
    
    def contains_rectangle(self, rect: 'Rect') -> bool:
        return self.lower_left.precedes(rect.lower_left) and self.upper_right.follows(rect.upper_right)

    def divide_vertically(self) -> Tuple['Rect', 'Rect']:
        midpoint = (self.lower_left.x + self.upper_right.x) / 2
        left = Rect((self.lower_left.x, self.lower_left.y), (midpoint, self.upper_right.y))
        right = Rect((midpoint, self.lower_left.y), (self.upper_right.x, self.upper_right.y))
        return left, right

    def divide_horizontally(self) -> Tuple['Rect', 'Rect']:
        midpoint = ((self.lower_left.y + self.upper_right.y) / 2)
        up = Rect((self.lower_left.x, midpoint), (self.upper_right.x, self.upper_right.y))
        down = Rect((self.lower_left.x, self.lower_left.y), (self.upper_right.x, midpoint))
        return up, down
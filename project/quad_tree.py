from typing import List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from utils.geometry import Point, Rect


class QuadTree():
    CAPACITY = 1  # Arbitrary constant to indicate how many elements can be stored in this quad tree node

    def __init__(self, bounding_box: Rect) -> 'QuadTree':
        self.bounding_box = bounding_box
        self.points: List[Point] = []

        self.upper_right: QuadTree = None
        self.upper_left: QuadTree = None
        self.lower_right: QuadTree = None
        self.lower_left: QuadTree = None

    def insert(self, point: Point):
        if not self.bounding_box.contains_point(point):
            return False
        if len(self.points) < QuadTree.CAPACITY and self.upper_right == None:
            self.points.append(point)
            return True
        if self.upper_right == None:
            self._subdivide()

        if self.upper_right.insert(point):
            return True
        if self.upper_left.insert(point):
            return True
        if self.lower_right.insert(point):
            return True
        if self.lower_left.insert(point):
            return True

        raise RuntimeError("Failed when inserting {}".format(point))

    def querry_range(self, rect: Rect) -> List[Point]:
        if not rect.intersects(self.bounding_box):
            return []

        result: List[Point] = list(
            filter(lambda point: rect.contains_point(point), self.points))
        if self.upper_right == None:
            return result

        result.extend(self.upper_right.querry_range(rect))
        result.extend(self.upper_left.querry_range(rect))
        result.extend(self.lower_right.querry_range(rect))
        result.extend(self.lower_left.querry_range(rect))
        return result

    def _subdivide(self):
        left, right = self.bounding_box.divide_vertically()
        up_left, down_left = left.divide_horizontally()
        up_right, down_right = right.divide_horizontally()

        self.upper_right = QuadTree(up_right)
        self.upper_left = QuadTree(up_left)
        self.lower_right = QuadTree(down_right)
        self.lower_left = QuadTree(down_left)

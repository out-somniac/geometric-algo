import random

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from quad_tree import QuadTree
from utils.geometry import Point, Rect
from utils.visualizer import visualizer


def main():
    points = [Point(random.uniform(0, 1), random.uniform(0, 1))
              for _ in range(100)]
    visualizer.visualize_result(points, Rect(
        (0.20, 0.20), (0.80, 0.80)), QuadTree)

    #rect = Rect((0.15, 0.15), (0.8, 0.8))
    #width = rect.upper_right.x - rect.lower_left.x
    #height = rect.upper_right.y - rect.lower_left.y
    # ax.add_patch(Rectangle((rect.lower_left.x, rect.lower_left.y),
    #                       width, height, fill=False, color='blue'))


if __name__ == "__main__":
    main()

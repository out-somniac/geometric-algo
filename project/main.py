import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import utils.generator as gen
from quad_tree import QuadTree
from utils.geometry import Point, Rect
from utils.visualizer import Visualizer


def main():
    #points = gen.normal_distribution(Rect((0.0, 0.0), (1.0, 1.0)), 1000)
    #points = gen.on_rectangle(Rect((0.0, 0.0), (1.0, 1.0)), 100)
    points = gen.rectangle_outliers(Rect((-1.0, -1.0), (1.0, 1.0)), 100)
    Visualizer.visualize_build(points, QuadTree)


if __name__ == "__main__":
    main()

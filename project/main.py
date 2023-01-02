import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import utils.generator as gen
from quad_tree import QuadTree
from utils.geometry import Point, Rect
from utils.visualizer import Visualizer
from KDtree import KDtree

from utils.files import FileHandler


def main():
    p = gen.normal_distribution(Rect((0.0, 0.0), (1.0, 1.0)), 1000)
    #points = gen.on_rectangle(Rect((0.0, 0.0), (1.0, 1.0)), 100)
    #points = gen.rectangle_outliers(Rect((-1.0, -1.0), (1.0, 1.0)), 100)
    #Visualizer.visualize_build(points, QuadTree)

    

    #points = gen.generate_grid(Rect((0.0, 0.0), (1.0, 1.0)), 100)
    #points = gen.generate_cross(Rect((0.0, 0.0), (1.0, 1.0)), 100)
    #points = gen.generate_circle(Point(0.0, 0.0), 100, 100)
    #Visualizer.visualize_build(points, KDtree)
    #Visualizer.visualize_result(points, Rect((50, 50), (100, 100)), KDtree)

    #FileHandler.save_points_to_file(points, "test.json")
    #points = FileHandler.get_saved_points("test.json")

if __name__ == "__main__":
    main()

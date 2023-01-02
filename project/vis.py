
from timeit import default_timer as timer
from utils.files import FileHandler
from utils.visualizer import Visualizer
from kdtree import KDtree
from quad_tree import QuadTree
from utils.generator import Generator as gen
from utils.geometry import Rect
from utils.geometry import Point
from time import time
import csv

def createQuad(points):
    tree = QuadTree(Rect.find_bounding_box(points))
    for p in points:
        tree.insert(p)
    return tree
    

def measure_quad_build_time(points):
    start = timer()
    createQuad(points)
    end = timer()
    res = end - start
    return res


def measure_kd_build_time(points):
    start = timer()
    KDtree(points)
    end = timer()
    res = end - start
    return res

def measure_kd_querry_time(points, rect):
    t = KDtree(points)
    start = timer()
    t.querry_range(rect)
    end = timer()
    res = end - start
    return res

def measure_quad_querry_time(points, rect):
    t = createQuad(points)
    start = timer()
    t.querry_range(rect)
    end = timer()
    res = end - start
    return res

def get_data_set(name, p_num):
    if name == "normal_dist":
        return gen.normal_distribution(Rect((0.0, 0.0), (1.0, 1.0)), p_num)
    elif name == "on_rectangle":
        return gen.on_rectangle(Rect((0.0, 0.0), (1.0, 1.0)), p_num)
    elif name == "outliers":
        return gen.rectangle_outliers(Rect((0.0, 0.0), (1.0, 1.0)), p_num, int(p_num / 10))
    elif name == "grid":
        return gen.generate_grid(Rect((0.0, 0.0), (1.0, 1.0)), p_num)
    elif name == "cross":
        return gen.generate_cross(Rect((0.0, 0.0), (1.0, 1.0)), p_num)
    elif name == "circle":
        return gen.generate_circle(Point(0.5, 0.5), 0.5, p_num)


def get_data_set_querry_range(name):
    if name == "normal_dist":
        return Rect((0.25, 0.25), (1.0, 0.60))
    elif name == "on_rectangle":
        return Rect((0.5, 0.0), (1.0, 1.0))
    elif name == "outliers":
        return Rect((0.5, 0.5), (3.0, 3.0))
    elif name == "grid":
        return Rect((0.25, 0.25), (0.7, 0.7))
    elif name == "cross":
        return Rect((0.25, 0.25), (0.75, 0.75))
    elif name == "circle":
        return Rect((0.5, 0.0), (1.0, 1.0))
    



def test_trees():
    points_num = [1000]
    data_set_names = ["normal_dist", "on_rectangle", "outliers", "grid", "cross", "circle"]

    for name in data_set_names:
        data_rows = [["points", "kd_build", "quad_build", "kd_querry", "quad_querry"]]
        points = get_data_set(name, 1000)
        Visualizer.visualize_build(points, KDtree)
        Visualizer.visualize_build(points, QuadTree)
        Visualizer.visualize_result(points, get_data_set_querry_range(name), KDtree)
        Visualizer.visualize_result(points, get_data_set_querry_range(name), QuadTree)

def main():
    test_trees()

if __name__ == "__main__":
    main()


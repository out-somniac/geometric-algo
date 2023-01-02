from utils.files import FileHandler
from utils.visualizer import Visualizer
from quad_tree import QuadTree
from kdtree import KDtree


def main():
    points = FileHandler.get_saved_points("example.json")
    Visualizer.visualize_result(points, QuadTree)
    Visualizer.visualize_result(points, KDtree)

if __name__ == "__main__":
    main()






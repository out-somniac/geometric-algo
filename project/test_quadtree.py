import random

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from quad_tree import QuadTree
from utils.geometry import Point, Rect


def main():
    def visualise(ax, tree: QuadTree):
        for point in tree.points:
            ax.plot(point.x, point.y, 'ro')

        if tree.upper_right == None:
            width = tree.bounding_box.upper_right.x - tree.bounding_box.lower_left.x
            height = tree.bounding_box.upper_right.y - tree.bounding_box.lower_left.y
            ax.add_patch(Rectangle((tree.bounding_box.lower_left.x,
                                    tree.bounding_box.lower_left.y), width, height, fill=False))
            return

        visualise(ax, tree.upper_right)
        visualise(ax, tree.upper_left)
        visualise(ax, tree.lower_left)
        visualise(ax, tree.lower_right)

    fig, ax = plt.subplots()

    tree = QuadTree(Rect((0, 0), (1, 1)))
    points = [Point(random.uniform(0, 1), random.uniform(0, 1))
              for _ in range(10)]
    for p in points:
        tree.insert(p)
    visualise(ax, tree)

    rect = Rect((0.15, 0.15), (0.8, 0.8))
    width = rect.upper_right.x - rect.lower_left.x
    height = rect.upper_right.y - rect.lower_left.y
    ax.add_patch(Rectangle((rect.lower_left.x, rect.lower_left.y),
                           width, height, fill=False, color='blue'))
    found = tree.querry_range(rect)
    print("Found {} point in range {}".format(len(found), rect))
    for point in found:
        ax.plot(point.x, point.y, marker='o', color='blue')
    plt.show()


if __name__ == "__main__":
    main()

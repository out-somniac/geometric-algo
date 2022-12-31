from typing import List, Tuple

from utils.drawing import LinesCollection, Plot, PointsCollection, Scene
from utils.geometry import Point, Rect


class Visualiser():
    @staticmethod
    def visualise_points(points: List[Point]):
        plot = Plot(scenes=[
            Scene(points=[PointsCollection(points=[tuple(p) for p in points])])
        ])

    @staticmethod
    def visualise_build(points: List[Point], tree):
        scenes: List[Scene] = tree.visualise_build(points)
        plot = Plot(scenes=scenes)
        plot.draw()

    @staticmethod
    def visualise_result(points: List[Point], rect: Rect, tree):
        scenes = tree.visualise_querry(points, rect)
        plot = Plot(scenes=scenes)
        plot.draw()

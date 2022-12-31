import math
from typing import List, Tuple

from numpy import random as rand

from utils.geometry import Point, Rect


def normal_distribution(bounds: Rect, total: int):
    middle: Point = Point(
        (bounds.upper_right.x + bounds.lower_left.x)/2,
        (bounds.upper_right.y + bounds.lower_left.y)/2)
    width = bounds.upper_right.x - bounds.lower_left.x
    height = bounds.upper_right.y - bounds.lower_left.y

    return [Point(rand.normal(loc=middle.x, scale=width/4), rand.normal(loc=middle.y, scale=height/4)) for _ in range(total)]


def on_rectangle(bounds: Rect, total: int):
    return on_polyline(bounds.get_polyline(), total)


def in_rectangle(bounds: Rect, total: int):
    return [Point(
        rand.uniform(bounds.lower_left.x, bounds.upper_right.x),
        rand.uniform(bounds.lower_left.y, bounds.upper_right.y))
        for _ in range(total)]


def rectangle_outliers(cluster_bounds: Rect, total_clustered: int, total_outliers=10):
    cluster_scale = 5.0
    outliers_bounds = Rect(
        (cluster_bounds.lower_left.x * cluster_scale,
         cluster_bounds.lower_left.y * cluster_scale),
        (cluster_bounds.upper_right.x * cluster_scale,
         cluster_bounds.upper_right.y * cluster_scale),
    )
    return in_rectangle(cluster_bounds, total_clustered) + in_rectangle(outliers_bounds, total_outliers)


def on_polyline(polyline: List[Tuple[float, float]], total):
    n = len(polyline)
    points_x, points_y = zip(*polyline)
    vectors = [(points_x[i+1] - points_x[i], points_y[i+1]-points_y[i])
               for i in range(n-1)]

    def norm(vec): return math.sqrt(vec[0]**2 + vec[1]**2)
    partial_sum = [0]
    for i in range(1, n):
        partial_sum.append(partial_sum[i-1] + norm(vectors[i-1]))
    total_sum = partial_sum[n-1]

    def one_rand(vectors, partial_sum, total_sum):
        t = rand.uniform(0, total_sum)
        i = 0
        while i < n:
            if (partial_sum[i]) <= t <= (partial_sum[i+1]):
                break
            i += 1
        theta = ((t-partial_sum[i])/norm(vectors[i]))
        final_x = points_x[i] + (points_x[i+1] - points_x[i]) * theta
        final_y = points_y[i] + (points_y[i+1] - points_y[i]) * theta
        return (final_x, final_y)
    return [one_rand(vectors, partial_sum, total_sum) for _ in range(total)]

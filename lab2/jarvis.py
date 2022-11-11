import matplotlib.pyplot as plt
import random
import math


def orientation(p, q, r, tolerance=10 ^ (-14)):
    determinant = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1]-q[1])
    if determinant > tolerance:
        return 1
    elif determinant < -tolerance:
        return -1
    else:
        return 0


def next_point(points, p):
    n = len(points)
    q = (p+1) % n
    for i in range(n):
        if orientation(points[p], points[i], points[q]) == -1:
            q = i
    return q


def get_leftmost(points):
    result = 0
    for i, point in enumerate(points):
        if point[0] < points[result][0]:
            result = i
    return result


def jarvis_march(points):
    leftmost = get_leftmost(points)
    hull = [leftmost]
    p = next_point(points, leftmost)
    while p != leftmost:
        hull.append(p)
        p = next_point(points, p)
    return hull


def rand_in_box(bounds_x, bounds_y, total):
    low_x, high_x = bounds_x
    low_y, high_y = bounds_y
    return [(random.uniform(low_x, high_x), random.uniform(low_y, high_y)) for _ in range(total)]


def rand_on_circle(origin, radius, total):
    def on_circle(t): return (org_x + radius * math.cos(t),
                              org_y + radius * math.sin(t))
    org_x, org_y = origin
    return [on_circle(random.uniform(0, 2*math.pi)) for _ in range(total)]


def plot_hull(hull, points, with_points=False):
    final = list(map(lambda i: points[i], hull))
    final.append(final[0])
    plt.plot(*zip(*final))
    if with_points:
        plt.scatter(*zip(*points))
        plt.show()


def main():
    points = rand_on_circle(origin=(0, 0), radius=10, total=20)
    plot_hull(jarvis_march(points), points, True)


if __name__ == "__main__":
    main()

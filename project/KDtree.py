class KDtree:
    class Region:
        def __init__(self, lower_left, upper_right):
            self.lower_left = lower_left
            self.upper_right = upper_right

    class Node:
        def __init__(self, point_idx):
            self.point_idx = point_idx
            self.left = None
            self.right = None
            self.region = None
            self.subtree_nodes = []

    def __init__(self, P):
        self.P = P
        self.points_indices = [i for i in range(len(P))]
        x_sorted = sorted(self.points_indices, key = lambda x : P[x][0])
        y_sorted = sorted(self.points_indices, key = lambda x : P[x][1])
        self.head = self._build_tree(x_sorted, y_sorted, 0)

    def _median(self, T):
        idx = ((len(T) - 1) // 2)
        return T[idx]

    def _find_region_lower_left(self, P, p_ind):
        x = min([P[i][0] for i in p_ind])
        y = min([P[i][1] for i in p_ind])
        return (x, y)

    def _find_region_upper_right(self, P, p_ind):
        x = max([P[i][0] for i in p_ind])
        y = max([P[i][1] for i in p_ind])
        return(x, y)

    def _build_tree(self, x_sorted, y_sorted, depth):
        if len(x_sorted) == 1:
            new_node =  self.Node(x_sorted[0])
            new_node.subtree_nodes = [x for x in x_sorted]
            new_node.region = self.Region(self.P[x_sorted[0]], self.P[x_sorted[0]])
            return new_node

        dim = depth % 2
        if dim == 0:
            mid_idx = self._median(x_sorted)
        else:
            mid_idx = self._median(y_sorted)
        
        x1_sorted = [p for p in x_sorted if self.P[p][dim] < self.P[mid_idx][dim] + eps]
        x2_sorted = [p for p in x_sorted if self.P[p][dim] > self.P[mid_idx][dim]]
        y1_sorted = [p for p in y_sorted if self.P[p][dim] < self.P[mid_idx][dim] + eps]
        y2_sorted = [p for p in y_sorted if self.P[p][dim] > self.P[mid_idx][dim]]
        
        new_node = self.Node(mid_idx)
        new_node.subtree_nodes = [x for x in x_sorted]
        region = self.Region(self._find_region_lower_left(self.P, x_sorted), self._find_region_upper_right(self.P, x_sorted))
        new_node.region = region

        new_node.left = self._build_tree(x1_sorted, y1_sorted, depth + 1)
        new_node.right = self._build_tree(x2_sorted, y2_sorted, depth + 1)
        return new_node

    def visualize_build_tree(self):
        min_x = min([self.P[i][0] for i in range(len(self.P))])
        min_y = min([self.P[i][1] for i in range(len(self.P))])
        max_x = max([self.P[i][0] for i in range(len(self.P))])
        max_y = max([self.P[i][1] for i in range(len(self.P))])
        bounds_lines = []
        bound_points = PointsCollection([(0, 0), (100, 0), (100, 100), (0, 100)], alpha = 0.0)
        scenes = []
        def _build_tree_vis(x_sorted, y_sorted, depth, bounds):
            if len(x_sorted) == 1:
                return self.Node(x_sorted[0])
            
            dim = depth % 2

            bounds_a = [b for b in bounds]
            bounds_b = [b for b in bounds]
            new_line = []
            
            if dim == 0:
                mid_idx = self._median(x_sorted)
                bounds_a[1] = (self.P[mid_idx][0], bounds[1][1])
                bounds_a[2] = (self.P[mid_idx][0], bounds[2][1])
                bounds_b[0] = (self.P[mid_idx][0], bounds[1][1])
                bounds_b[3] = (self.P[mid_idx][0], bounds[2][1])
                new_line = [bounds_a[1], bounds_a[2]]
            else:
                mid_idx = self._median(y_sorted)
                bounds_b[0] = (bounds[0][0], self.P[mid_idx][1])
                bounds_b[1] = (bounds[1][0], self.P[mid_idx][1])
                bounds_a[2] = (bounds[2][0], self.P[mid_idx][1])
                bounds_b[3] = (bounds[3][0], self.P[mid_idx][1])
                new_line = [bounds_b[0], bounds_b[1]]

            bounds_lines.append(new_line)
            
            x1_sorted = [p for p in x_sorted if self.P[p][dim] < self.P[mid_idx][dim] + eps]
            x2_sorted = [p for p in x_sorted if self.P[p][dim] > self.P[mid_idx][dim]]
            y1_sorted = [p for p in y_sorted if self.P[p][dim] < self.P[mid_idx][dim] + eps]
            y2_sorted = [p for p in y_sorted if self.P[p][dim] > self.P[mid_idx][dim]]
            
            new_node = self.Node(mid_idx)
            new_node.lower_left = self._find_region_lower_left(self.P, x_sorted)
            new_node.upper_right = self._find_region_upper_right(self.P, x_sorted)

            scenes.append(
                Scene(points = \
                                [PointsCollection(self.P)] + \
                                [PointsCollection([self.P[p]for p in x_sorted], color = 'orange')] + \
                                [PointsCollection([self.P[mid_idx]], color = 'red')] + \
                                [PointsCollection([new_node.lower_left, new_node.upper_right], color = 'green')] + \
                                [bound_points],
                        lines = \
                            [LinesCollection([l for l in bounds_lines])])
            )

            new_node.left = _build_tree_vis(x1_sorted, y1_sorted, depth + 1, bounds_a)
            new_node.right = _build_tree_vis(x2_sorted, y2_sorted, depth + 1, bounds_b)
            return new_node

        x_sorted = sorted(self.points_indices, key = lambda x : self.P[x][0])
        y_sorted = sorted(self.points_indices, key = lambda x : self.P[x][1])
        bounds = [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
        bounds_lines = [[bounds[0], bounds[1]], [bounds[1], bounds[2]], [bounds[2], bounds[3]], [bounds[3], bounds[0]]]
        #scenes.append(Scene(points = [PointsCollection(self.P)], lines = [LinesCollection(bounds_lines)]))
        head = _build_tree_vis(x_sorted, y_sorted, 0, bounds)
        return scenes

    def _intersect(self, p1, p2):
            new_lower_left = (max(p1.lower_left[0], p2.lower_left[0]), max(p1.lower_left[1], p2.lower_left[1]))
            new_upper_right = (min(p1.upper_right[0], p2.upper_right[0]), min(p1.upper_right[1], p2.upper_right[1]))
            new = self.Region(new_lower_left, new_upper_right)

            if self._contains(p1, new) and self._contains(p2, new):
                return True
            return False
            
    def _contains(self, p1, p2):
        if p1.lower_left[0] - eps <= p2.lower_left[0] and p1.lower_left[1] - eps <= p2.lower_left[1] and \
            p1.upper_right[0] + eps >= p2.upper_right[0] and p1.upper_right[1] + eps >= p2.upper_right[1]:
            return True
        return False

    def get_points_inside(self, x1, x2, y1, y2):
        def _query(r, head):
            if head.left == None and head.right == None:
                return []
            
            res = []
            if self._contains(r, head.left.region):
                res += head.left.subtree_nodes
            elif self._intersect(r, head.left.region):
                res += _query(r, head.left)

            if self._contains(r, head.right.region):
                res += head.right.subtree_nodes
            elif self._intersect(r, head.right.region):
                res += _query(r, head.right)
            return res

        r_lower_left = (min(x1, x2), min(y1, y2))
        r_upper_right = (max(x1, x2), max(y1, y2))
        r = self.Region(r_lower_left, r_upper_right)
        res = _query(r, self.head)
        return res
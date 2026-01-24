from typing import List, Tuple

coords: List[Tuple[int, int]] = [
    tuple(map(int, line.split(","))) for line in open("input.txt").read().splitlines()
]
num_points: int = len(coords)

area_p1: int = 0
area_p2: int = 0

edges: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [
    (coords[i], coords[(i + 1) % num_points]) for i in range(num_points)
]


def is_contained(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Checks if the rectangle defined by corners (x1, y1) and (x2, y2)
    is fully contained within the polygon defined by 'edges'.
    """
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    # We do the check by seeing if any of the polygon edges pass inside the rectangle
    # If yes, then the rectangle exits the polygon and is not contained
    for (ux, uy), (vx, vy) in edges:
        if ux == vx:
            if xmin < ux < xmax:
                edge_min_y, edge_max_y = min(uy, vy), max(uy, vy)
                # Check for interval overlap between the range of the edge and the rectangle
                if edge_min_y < ymax and ymin < edge_max_y:
                    return False
        else:
            if ymin < uy < ymax:
                edge_min_x, edge_max_x = min(ux, vx), max(ux, vx)
                if edge_min_x < xmax and xmin < edge_max_x:
                    return False

    # We now check if the midpoint of the rectangle is inside the polygon using the ray casting algorithm
    # (https://en.wikipedia.org/wiki/Point_in_polygon)
    mid_x: int = (xmin + xmax) / 2
    mid_y: int = (ymin + ymax) / 2
    intersections: int = 0

    # We will cast a ray downwards and count the intersections with horizontal lines
    for (ux, uy), (vx, vy) in edges:
        if uy == vy < mid_y and (ux <= mid_x < vx or vx <= mid_x < ux):
            intersections += 1

    return intersections % 2 == 1


for i in range(num_points):
    for j in range(i + 1, num_points):
        p1, p2 = coords[i], coords[j]

        # Calculate Area (inclusive of tiles, so +1)
        width = abs(p1[0] - p2[0]) + 1
        height = abs(p1[1] - p2[1]) + 1
        current_area = width * height

        area_p1 = max(area_p1, current_area)

        if current_area > area_p2 and is_contained(p1[0], p1[1], p2[0], p2[1]):
            area_p2 = current_area


print(area_p1, area_p2)

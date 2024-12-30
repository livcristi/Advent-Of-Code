from collections import defaultdict
from collections import deque
from typing import Optional

# filename = "test-data.txt"


filename = "data.txt"


def get_region_value(region_data: list[list[str]], row: int, col: int) -> Optional[str]:
    if row < 0 or row >= len(region_data) or col < 0 or col >= len(region_data[row]):
        return None
    return region_data[row][col]


def find_area_perimeter(
    region_data: list[list[str]], seen_data: list[list[bool]], row: int, col: int
) -> tuple[int, int]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen_queue = {(row, col)}
    seen_data[row][col] = True
    total_perimeter = 0
    total_area = 0
    while len(seen_queue) > 0:
        current_row, current_col = seen_queue.pop()
        seen_data[current_row][current_col] = True
        total_area += 1
        for dx, dy in directions:
            new_row, new_col = current_row + dx, current_col + dy
            if (
                get_region_value(region_data, new_row, new_col) is None
                or get_region_value(region_data, new_row, new_col)
                != region_data[row][col]
            ):
                total_perimeter += 1
            elif not seen_data[new_row][new_col]:
                seen_queue.add((new_row, new_col))
    return total_area, total_perimeter


def compute_price_regions(region_data: list[list[str]]) -> int:
    seen_data = [
        [False for _ in range(len(region_data[0]))] for _ in range(len(region_data))
    ]
    total_sum = 0
    for row in range(len(region_data)):
        for col in range(len(region_data[row])):
            if not seen_data[row][col]:
                area, perimeter = find_area_perimeter(region_data, seen_data, row, col)
                total_sum += area * perimeter
    return total_sum


def get_subregions(coordinates: list[tuple[int, int]]) -> int:
    # Create a set for fast lookup and a dictionary for adjacency lists
    point_set = set(coordinates)
    visited = set()

    # Directions for horizontal and vertical neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start):
        queue = deque([start])
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor in point_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Count connected components
    region_count = 0
    for coordinate in coordinates:
        if coordinate not in visited:
            visited.add(coordinate)
            bfs(coordinate)
            region_count += 1

    return region_count


def find_area_sides(
    region_data: list[list[str]], seen_data: list[list[bool]], row: int, col: int
) -> tuple[int, int]:
    # right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seen_queue = {(row, col)}
    seen_data[row][col] = True
    total_area = 0
    sides_mapping = defaultdict(list)
    while len(seen_queue) > 0:
        current_row, current_col = seen_queue.pop()
        seen_data[current_row][current_col] = True
        total_area += 1
        for dx, dy in directions:
            new_row, new_col = current_row + dx, current_col + dy
            if (
                get_region_value(region_data, new_row, new_col) is None
                or get_region_value(region_data, new_row, new_col)
                != region_data[row][col]
            ):
                if dx == 0:
                    sides_mapping[(0, new_col, dx, dy)].append(
                        (current_row, current_col)
                    )
                else:
                    sides_mapping[(new_row, 0, dx, dy)].append(
                        (current_row, current_col)
                    )
            elif not seen_data[new_row][new_col]:
                seen_queue.add((new_row, new_col))
    total_sides = 0
    for _, side_elements in sides_mapping.items():
        total_sides += get_subregions(side_elements)
    return total_area, total_sides


def compute_price_regions_sides(region_data: list[list[str]]) -> int:
    seen_data = [
        [False for _ in range(len(region_data[0]))] for _ in range(len(region_data))
    ]
    total_sum = 0
    for row in range(len(region_data)):
        for col in range(len(region_data[row])):
            if not seen_data[row][col]:
                area, sides = find_area_sides(region_data, seen_data, row, col)
                total_sum += area * sides
    return total_sum


with open(filename) as f_inp:
    map_data = list(line.strip() for line in f_inp.readlines())
    print(compute_price_regions(map_data))
    print(compute_price_regions_sides(map_data))

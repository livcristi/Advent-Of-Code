# filename = "test-data.txt"


filename = "data.txt"


def get_score(height_map: list[list[int]], row: int, col: int) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    seen_map = {(row, col)}
    seen_queue = {(row, col, height_map[row][col])}
    total = 0
    while len(seen_queue) > 0:
        x, y, val = seen_queue.pop()
        if val == 9:
            total += 1
        seen_map.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(height_map)
                and 0 <= new_y < len(height_map[0])
                and height_map[new_x][new_y] == val + 1
                and (new_x, new_y) not in seen_map
            ):
                seen_queue.add((new_x, new_y, height_map[new_x][new_y]))
    return total


def get_score_all(height_map: list[list[int]], row: int, col: int) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    seen_queue = [(row, col, height_map[row][col])]
    total = 0
    while len(seen_queue) > 0:
        x, y, val = seen_queue.pop()
        if val == 9:
            total += 1
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < len(height_map)
                and 0 <= new_y < len(height_map[0])
                and height_map[new_x][new_y] == val + 1
            ):
                seen_queue.append((new_x, new_y, height_map[new_x][new_y]))
    return total


def count_scores(height_map: list[list[int]]) -> int:
    total = 0
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if height_map[row][col] == 0:
                total += get_score(height_map, row, col)
    return total


def count_better_scores(height_map: list[list[int]]) -> int:
    total = 0
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if height_map[row][col] == 0:
                total += get_score_all(height_map, row, col)
    return total


with open(filename, "r") as f_inp:
    map_data = [
        list(map(int, [char for char in line.strip()])) for line in f_inp.readlines()
    ]
    print(count_scores(map_data))
    print(count_better_scores(map_data))

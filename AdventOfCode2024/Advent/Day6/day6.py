# filename = "test-data.txt"

filename = "data.txt"


def find_guard_position(map_data: list[list[str]]) -> tuple[int, int]:
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] in ["^", ">", "v", "<"]:
                return i, j
    return None


def guard_in_perimeter(
    map_data: list[list[str]], guard_position: tuple[int, int]
) -> bool:
    return 0 <= guard_position[0] < len(map_data) and 0 <= guard_position[1] < len(
        map_data[0]
    )


def get_value(map_data: list[list[str]], row: int, column: int) -> str:
    return (
        map_data[row][column]
        if 0 <= row < len(map_data) and 0 <= column < len(map_data[0])
        else ""
    )


def count_positions(map_data: list[list[str]]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    guard_position = find_guard_position(map_data)
    guard_direction = 0
    walked_positions = set()
    while guard_in_perimeter(map_data, guard_position):
        walked_positions.add(guard_position)
        new_position = (
            guard_position[0] + directions[guard_direction][0],
            guard_position[1] + directions[guard_direction][1],
        )
        if get_value(map_data, new_position[0], new_position[1]) != "#":
            guard_position = new_position
        else:
            guard_direction = (guard_direction + 1) % 4
    return len(walked_positions)


def can_guard_get_stuck(map_data: list[list[str]]) -> bool:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    guard_position = find_guard_position(map_data)
    guard_direction = 0
    walked_states = set()
    while guard_in_perimeter(map_data, guard_position):
        new_state = (guard_direction, guard_position[0], guard_position[1])
        if new_state in walked_states:
            return True
        walked_states.add(new_state)
        new_position = (
            guard_position[0] + directions[guard_direction][0],
            guard_position[1] + directions[guard_direction][1],
        )
        if get_value(map_data, new_position[0], new_position[1]) == "":
            return False
        if get_value(map_data, new_position[0], new_position[1]) != "#":
            guard_position = new_position
        else:
            guard_direction = (guard_direction + 1) % 4
    return True


def count_stuck_positions(map_data: list[list[str]]) -> int:
    total = 0
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == ".":
                map_data[row][col] = "#"
                total += can_guard_get_stuck(map_data)
                map_data[row][col] = "."
    return total


with open(filename) as f:
    map_file_data = [[char for char in line.strip()] for line in f.readlines()]
    print(count_positions(map_file_data))
    print(count_stuck_positions(map_file_data))

# filename = "test-data.txt"


filename = "data.txt"


def get_value(word_map: list[list[str]], row: int, col: int) -> int:
    return word_map[row][col] if 0 <= row < len(word_map) and 0 <= col < len(word_map[0]) else ""


def count_xmas_directions(word_map: list[list[str]], row: int, col: int) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    return sum(
        all(get_value(word_map, row + k * di, col + k * dj) == word
            for k, word in enumerate("XMAS"))
        for di, dj in directions
    )


def count_mas_directions(word_map: list[list[str]], row: int, col: int) -> int:
    if get_value(word_map, row, col) != 'A':
        return 0
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    matches = [get_value(word_map, row + di, col + dj) for di, dj in directions]
    return matches.count('M') == 2 and matches.count('S') == 2 and matches[0] != matches[3]


def count_xmas(word_map: list[list[str]]) -> int:
    return sum(count_xmas_directions(word_map, i, j)
               for i in range(len(word_map))
               for j in range(len(word_map[0])))


def count_mas(word_map: list[list[str]]) -> int:
    return sum(count_mas_directions(word_map, i, j)
               for i in range(len(word_map))
               for j in range(len(word_map[0])))


with open(filename, "r") as f_inp:
    file_data = [line.strip() for line in f_inp.readlines()]
    print(count_xmas(file_data))
    print(count_mas(file_data))

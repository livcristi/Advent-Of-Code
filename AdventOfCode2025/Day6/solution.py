from typing import List, Tuple
from math import prod

lines: List[str] = open("input.txt").read().splitlines()
max_len: int = max(len(line) for line in lines)

ops_line: str = lines[-1]
grid: List[str] = lines[:-1]


def solve_part1() -> int:
    # Extract numbers by parsing each line normally
    matrix: List[List[int]] = []
    for line in grid:
        nums = [int(x) for x in line.split() if x.strip()]
        if nums:
            matrix.append(nums)

    ops: List[str] = [x for x in ops_line.split() if x.strip()]

    total: int = 0
    num_cols: int = len(matrix[0])

    for c in range(num_cols):
        col_values = [row[c] for row in matrix]
        if ops[c] == "*":
            total += prod(col_values)
        else:
            total += sum(col_values)

    return total


def solve_part2() -> int:
    total: int = 0
    cols: int = max_len
    rows: int = len(grid)

    problem_ranges: List[Tuple[int, int]] = []
    start: int = 0

    # Find each block of operations
    while start < cols:
        # Skip leading empty columns
        while start < cols and all(grid[r][start] == " " for r in range(rows)):
            start += 1

        if start >= cols:
            break

        end = start
        while end < cols and any(grid[r][end] != " " for r in range(rows)):
            end += 1

        problem_ranges.append((start, end))
        start = end

    # Process each block individually, respecting the cephalopods math
    for start, end in problem_ranges:
        op_char: str = "+"
        for c in range(start, end):
            if ops_line[c] in ("+", "*"):
                op_char = ops_line[c]
                break

        numbers: List[int] = []

        for c in range(end - 1, start - 1, -1):
            digits: str = ""
            for r in range(rows):
                char = grid[r][c]
                if char.isdigit():
                    digits += char

            if digits:
                numbers.append(int(digits))

        if op_char == "*":
            total += prod(numbers)
        else:
            total += sum(numbers)

    return total


print(solve_part1(), solve_part2())

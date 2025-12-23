from collections import defaultdict

from typing import List, Set, Dict

grid: List[str] = open("input.txt").read().splitlines()

num_rows: int = len(grid)
num_cols: int = len(grid[0])

start_col: int = grid[0].find("S")

# We will keep a DP array for the number of timelines present at each point (which we will sum at the end)
dp: Dict[tuple, int] = defaultdict(int)
dp[(0, start_col)] = 1
timelines = 0

# We will also keep track of the visited splitters, since they are needed for part 1
visited_splitters: int = 0

for row_index in range(num_rows):
    for col_index in range(num_cols):
        # Just skip the current position if there is are no timelines hitting it
        if not (timeline_count := dp[(row_index, col_index)]):
            continue

        current_char: str = grid[row_index][col_index]

        # When we are at the last row, we need to sum the total timelines for part 2
        if row_index == num_rows - 1:
            if current_char == "^":
                timelines += 2 * timeline_count
                visited_splitters += 1
            else:
                timelines += timeline_count
            continue

        if current_char == "S" or current_char == "." or current_char == "|":
            # Pass down the timeline value
            dp[(row_index + 1, col_index)] += timeline_count
        elif current_char == "^":
            # Split the timeline value on the left and right
            dp[(row_index + 1, col_index - 1)] += timeline_count
            dp[(row_index + 1, col_index + 1)] += timeline_count
            visited_splitters += 1

print(visited_splitters, timelines)

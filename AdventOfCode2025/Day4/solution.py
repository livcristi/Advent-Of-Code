from typing import List

raw_lines: List[str] = open("input.txt").read().splitlines()
grid: List[List[int]] = (
    [[0] * (len(raw_lines[0]) + 2)]
    + [[0] + [int(c == "@") for c in line] + [0] for line in raw_lines]
    + [[0] * (len(raw_lines[0]) + 2)]
)


# Finally got to write a convolutions function and actually use it >:3
def convolution_2d(
    mat: List[List[int]], kernel_mat: List[List[int]]
) -> List[List[int]]:
    mat_rows, mat_cols = len(mat), len(mat[0])
    kern_rows, kern_cols = len(kernel_mat), len(kernel_mat[0])
    res_rows, res_cols = mat_rows - kern_rows + 1, mat_cols - kern_cols + 1

    result: List[List[int]] = [[0] * res_cols for _ in range(res_rows)]

    for r in range(res_rows):
        for c in range(res_cols):
            value: int = 0
            for kr in range(kern_rows):
                for kc in range(kern_cols):
                    value += mat[r + kr][c + kc] * kernel_mat[kr][kc]
            result[r][c] = value

    return result


total: int = 0
total_2: int = 0
can_remove: bool = True
kernel: List[List[int]] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# We will just keep trying to remove values for which the conv value is less than 4, until we can no longer remove them
while can_remove:
    conv_result = convolution_2d(grid, kernel)
    rows, cols = len(conv_result), len(conv_result[0])

    current_removed: int = 0
    new_grid: List[List[int]] = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            grid_r, grid_c = r + 1, c + 1

            if grid[grid_r][grid_c] == 0:
                continue

            if conv_result[r][c] < 4:
                new_grid[grid_r][grid_c] = 0
                current_removed += 1

    grid = new_grid

    if current_removed == 0:
        can_remove = False

    if total == 0:
        total = current_removed
    total_2 += current_removed

print(total, total_2)

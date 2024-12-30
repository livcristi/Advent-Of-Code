import re

# filename = "test-data.txt"


filename = "data.txt"


def solve_equation(equations_data):
    determinant = (
        equations_data[0] * equations_data[3] - equations_data[1] * equations_data[2]
    )
    if determinant != 0:
        part_x = (
            equations_data[4] * equations_data[3]
            - equations_data[5] * equations_data[1]
        ) / determinant
        part_y = (
            equations_data[0] * equations_data[5]
            - equations_data[2] * equations_data[4]
        ) / determinant
        if int(part_x) != part_x or int(part_y) != part_y:
            return None, None
        return int(part_x), int(part_y)
    return None, None


def find_buttons_scores(buttons_data: list[tuple]) -> int:
    total = 0
    for buttons in buttons_data:
        sol_x, sol_y = solve_equation(buttons)
        if sol_x is None:
            continue
        total += sol_x * 3 + sol_y
    return total


def find_buttons_scores_broken(buttons_data: list[tuple]) -> int:
    total = 0
    for buttons in buttons_data:
        buttons[4] += 10000000000000
        buttons[5] += 10000000000000
        sol_x, sol_y = solve_equation(buttons)
        if sol_x is None:
            continue
        total += sol_x * 3 + sol_y
    return total


with open(filename, "r") as f_inp:
    buttons_raw_data = f_inp.read().split("\n\n")
    buttons_actual_data = []
    for line in buttons_raw_data:
        a_data = list(map(int, list(*re.findall(r"Button A: X\+(.*), Y\+(.*)", line))))
        b_data = list(map(int, list(*re.findall(r"Button B: X\+(.*), Y\+(.*)", line))))
        sol_data = list(map(int, list(*re.findall(r"Prize: X=(.*), Y=(.*)", line))))
        buttons_actual_data.append(
            [a_data[0], b_data[0], a_data[1], b_data[1], sol_data[0], sol_data[1]]
        )
    print(find_buttons_scores(buttons_actual_data))
    print(find_buttons_scores_broken(buttons_actual_data))

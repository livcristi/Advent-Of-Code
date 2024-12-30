import re
from math import prod

from tqdm import tqdm
import os
from PIL import Image

# filename = "test-data.txt"


filename = "data.txt"


def debug_map(robots_data, max_height, max_width):
    temp_map = [[0] * max_width for _ in range(max_height)]
    for robot_data in robots_data:
        temp_map[robot_data[1]][robot_data[0]] += 1
    for x in range(max_height):
        for y in range(max_width):
            print(temp_map[x][y], end="")
        print()
    print()


def save_map_as_image(robots_data, max_height, max_width, filename):
    temp_map = [[0] * max_width for _ in range(max_height)]
    for robot_data in robots_data:
        temp_map[robot_data[1]][robot_data[0]] = 1
    new_img = Image.new("L", (max_width, max_height))
    pixels = new_img.load()
    for y in range(max_height):
        for x in range(max_width):
            pixels[x, y] = 255 if temp_map[y][x] > 0 else 0
    new_img.save(filename)


def compute_quadrants_counts(robots_data, max_height, max_width):
    quadrants = [0, 0, 0, 0]
    for robot_data in robots_data:
        if robot_data[0] == max_width // 2 or robot_data[1] == max_height // 2:
            continue
        x_data = robot_data[0] < max_width // 2
        y_data = robot_data[1] < max_height // 2
        if x_data and y_data:
            quadrants[0] += 1
        elif x_data and not y_data:
            quadrants[1] += 1
        elif not x_data and y_data:
            quadrants[2] += 1
        else:
            quadrants[3] += 1
    return quadrants


def compute_robots_positions(
    robots_data, max_height=103, max_width=101, epochs=100, debug=False
) -> int:
    robots_data_copy = robots_data.copy()
    for index in tqdm(range(epochs)):
        if debug:
            save_map_as_image(robots_data_copy, max_height, max_width, f"{index}.png")
        for robot_data in robots_data_copy:
            new_x = robot_data[0] + robot_data[2]
            new_x = new_x if 0 <= new_x < max_width else (new_x + max_width) % max_width
            new_y = robot_data[1] + robot_data[3]
            new_y = (
                new_y if 0 <= new_y < max_height else (new_y + max_height) % max_height
            )
            robot_data[0], robot_data[1] = new_x, new_y
    if debug:
        file_sizes = {}
        # traverse all images on disk and print the top 10 with the lowest size
        for index in range(epochs):
            file_size = os.stat(f"{index}.png").st_size
            file_sizes[index] = file_size
        sorted_data = sorted(file_sizes.items(), key=lambda x: x[1])
        print(sorted_data[:50])
    return prod(compute_quadrants_counts(robots_data_copy, max_height, max_width))


with open(filename, "r") as f_inp:
    robots_raw_data = [
        list(map(int, *re.findall("p=(.*),(.*) v=(.*),(.*)", line)))
        for line in f_inp.readlines()
    ]
    print(compute_robots_positions(robots_raw_data, 103, 101, 100, debug=False))
    print(compute_robots_positions(robots_raw_data, 103, 101, 10000, debug=True))

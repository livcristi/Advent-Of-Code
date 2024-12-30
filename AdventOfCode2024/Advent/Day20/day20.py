from itertools import combinations

# filename = "test-data.txt"

filename = "data.txt"

with open(filename, "r") as f_inp:
    grid_data = {col + row * 1j: char for row, row_data in enumerate(f_inp)
                 for col, char in enumerate(row_data.strip()) if char != '#'}

    start = next(pos for pos in grid_data if grid_data[pos] == 'S')

    directions = [1, -1j, -1, 1j]
    lee_queue = [start]
    dist = {start: 0}
    while len(lee_queue) > 0:
        element = lee_queue.pop(0)
        for direction in directions:
            if element + direction in grid_data and element + direction not in dist:
                dist[element + direction] = dist[element] + 1
                lee_queue.append(element + direction)

    cheats_part_1 = 0
    cheats_part_2 = 0
    for (start_cheat, dist_start), (end_cheat, dist_end) in combinations(dist.items(), 2):
        cheat_distance = abs((start_cheat - end_cheat).real) + abs((start_cheat - end_cheat).imag)
        if cheat_distance == 2 and dist_end - dist_start - cheat_distance >= 100:
            cheats_part_1 += 1
        if cheat_distance <= 20 and dist_end - dist_start - cheat_distance >= 100:
            cheats_part_2 += 1

    print(cheats_part_1)
    print(cheats_part_2)

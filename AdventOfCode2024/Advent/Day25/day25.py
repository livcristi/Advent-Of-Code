# filename = "test-data.txt"

filename = "data.txt"

with open(filename, "r") as f_inp:
    schematics_data = f_inp.read().split("\n\n")
    locks = []
    keys = []
    for schematics in schematics_data:
        rows = schematics.split("\n")
        heights = [-1] * 5
        for i, row in enumerate(rows):
            for j, char in enumerate(row):
                if char == "#":
                    heights[j] += 1
        if rows[0] == "#####":
            locks.append(heights)
        else:
            keys.append(heights)
    total = sum(sum(all(k + l <= 5 for k, l in zip(key, lock)) for lock in locks) for key in keys)

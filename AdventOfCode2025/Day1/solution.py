with open("input.txt") as f_inp:
    entries: list[int] = [
        (1 if line[0] == "R" else -1) * int(line[1:])
        for line in f_inp.read().splitlines()
        if line
    ]

safe_val = 50
total = 0
total_2 = 0
for entry in entries:
    for _ in range(abs(entry)):
        if entry < 0:
            safe_val -= 1
            safe_val = (safe_val + 100) % 100
            if safe_val == 0:
                total_2 += 1
        else:
            safe_val += 1
            safe_val = safe_val % 100
            if safe_val == 0:
                total_2 += 1
    if safe_val == 0:
        total += 1
print(total, total_2)

def solve_problem(inp_file, is_part_2=False):
    elves_calories = []
    amount = 0
    for line in inp_file.readlines():
        if len(line) > 1:
            amount += int(line.strip())
        else:
            elves_calories.append(amount)
            amount = 0
    if amount > 0:
        elves_calories.append(amount)
    if not is_part_2:
        return max(elves_calories)
    else:
        elves_calories.sort()
        return sum(elves_calories[-3:])


with open('input.txt', 'r') as inp:
    print(solve_problem(inp, True))

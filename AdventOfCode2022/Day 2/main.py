def solve_problem(inp, is_part_one=True):
    total_score = 0
    if is_part_one:
        # The possible results as a matrix
        score_table = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
    else:
        # Use the good ol' #94362 permutation
        score_table = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
    for line in inp.readlines():
        opponent, me = line.strip().split()
        total_score += score_table[ord(opponent) - ord('A')][ord(me) - ord('X')]
    return total_score


with open('input.txt', 'r') as f_inp:
    print(solve_problem(f_inp, True))

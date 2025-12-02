from typing import List, Tuple, Set

ranges: List[Tuple[int, int]] = [
    (int(start), int(end))
    for start, end in (
        item.split("-")
        for item in open("input.txt").read().replace("\n", "").split(",")
        if item.strip()
    )
]

max_val: int = max(r[1] for r in ranges)


def is_in_range(value: int) -> bool:
    for start, end in ranges:
        if start <= value <= end:
            return True
    return False


rep_1: Set[int] = set()
rep_2: Set[int] = set()


for init in range(1, 10 ** 5):
    str_init: str = str(init)

    # Part 1: check if the repeated substring id is in any range
    id1: int = int(str_init * 2)

    # We can optimize by breaking earlier if we reach a value greater than our largest interval end
    if id1 > max_val:
        break

    if is_in_range(id1):
        rep_1.add(id1)

    # Part 2: check multiple repetitions
    rep: int = 2
    id2: int = int(str_init * rep)

    while id2 <= max_val:
        if is_in_range(id2):
            rep_2.add(id2)
        rep += 1
        id2 = int(str_init * rep)

print(sum(rep_1), sum(rep_2))

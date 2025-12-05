from typing import List, Tuple

raw_sections: List[str] = open("input.txt").read().split("\n\n")

ranges: List[Tuple[int, int]] = sorted(
    [
        (int(p[0]), int(p[1]))
        for p in (line.split("-") for line in raw_sections[0].splitlines())
    ],
    key=lambda x: x[0],
)

ingredients: List[int] = [
    int(line) for line in raw_sections[1].splitlines() if line.strip()
]

uniq_ranges: List[Tuple[int, int]] = [ranges[0]]

# We first sort the ranges, then merge them with the last one, to generate the disjoint ranges, needed to find the number of possible ingredients
for start, end in ranges[1:]:
    prev_start, prev_end = uniq_ranges[-1]
    if start <= prev_end:
        uniq_ranges[-1] = (prev_start, max(prev_end, end))
    else:
        uniq_ranges.append((start, end))

ranges = uniq_ranges


def is_ing_good(ingredient: int) -> bool:
    return any(
        range_start <= ingredient <= range_end for range_start, range_end in ranges
    )


total: int = sum(is_ing_good(ing) for ing in ingredients)
total_2: int = sum(end - start + 1 for start, end in ranges)

print(total)
print(total_2)

from typing import List

batteries: List[List[int]] = [
    list(map(int, line.strip())) for line in open("input.txt")
]


def list_to_int(digits: List[int]) -> int:
    return int("".join(map(str, digits)))


def get_max_subsequence(array: List[int], length: int) -> List[int]:
    stack: List[int] = []
    drop_count: int = len(array) - length

    for val in array:
        # While the current value is bigger than the last value we kept,
        # and we still have "drops" available, remove the smaller previous value.
        while drop_count > 0 and stack and stack[-1] < val:
            stack.pop()
            drop_count -= 1
        stack.append(val)

    return stack[:length]


total: int = 0
total_2: int = 0

for bank in batteries:
    total += list_to_int(get_max_subsequence(bank, 2))
    total_2 += list_to_int(get_max_subsequence(bank, 12))

print(total, total_2)

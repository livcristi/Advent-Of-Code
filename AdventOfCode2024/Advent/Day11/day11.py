from collections import Counter

# filename = "test-data.txt"

filename = "data.txt"


def stones_count(stones_data: list[int], blink_times=25) -> int:
    stones = Counter(stones_data)
    for _ in range(blink_times):
        new_stones = Counter()
        for key, value in stones.items():
            if key == 0:
                new_stones[1] += value
            elif len(str(key)) % 2 == 0:
                mid = len(str(key)) // 2
                new_stones[int(str(key)[:mid])] += value
                new_stones[int(str(key)[mid:])] += value
            else:
                new_stones[key * 2024] += value
        stones = new_stones
    return sum(stones.values())


with open(filename, "r") as f_inp:
    stores_data = list(map(int, f_inp.read().split(" ")))
    print(stones_count(stores_data, blink_times=25))
    print(stones_count(stores_data, blink_times=75))

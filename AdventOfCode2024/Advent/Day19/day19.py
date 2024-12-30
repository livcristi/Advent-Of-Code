from functools import lru_cache

# filename = "test-data.txt"


filename = "data.txt"


def count_valid(patterns, towels):
    @lru_cache(maxsize=None)
    def is_towel_valid(towel):
        if towel in patterns:
            return True
        for index in range(len(towel)):
            if towel[:index] in patterns:
                result = is_towel_valid(towel[index:])
                if result:
                    return True
        return False

    return sum(is_towel_valid(towel) for towel in towels)


def count_all_possibilities(patterns, towels):
    @lru_cache(maxsize=None)
    def towel_count(towel):
        if towel is None or len(towel) == 0:
            return 0
        count = 0
        if towel in patterns:
            count += 1
        for index in range(len(towel)):
            if towel[:index] in patterns:
                count += towel_count(towel[index:])
        return count

    return sum(towel_count(towel) for towel in towels)


with open(filename, "r") as f_inp:
    patterns_data, towels_data = f_inp.read().split("\n\n")
    patterns_data = [pattern.strip() for pattern in patterns_data.split(",")]
    towels_data = [towel.strip() for towel in towels_data.split("\n")]
    print(count_valid(patterns_data, towels_data))
    print(count_all_possibilities(patterns_data, towels_data))

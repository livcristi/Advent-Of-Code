from collections import defaultdict

# filename = "test-data.txt"


filename = "data.txt"


def pairwise(iterable):
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b


def simulate_market(secret, iteration_count):
    for _ in range(iteration_count):
        secret = (secret * 64 ^ secret) % 16777216
        secret = (secret // 32 ^ secret) % 16777216
        secret = (secret * 2048 ^ secret) % 16777216
    return secret


def simulate_first_phase(initial_values):
    return sum(simulate_market(initial_value, 2000) for initial_value in initial_values)


def simulate_second_phase(initial_values):
    patterns = defaultdict(int)
    for initial_value in initial_values:
        numbers = [initial_value] + [initial_value := simulate_market(initial_value, 1) for _ in range(2000)]
        differences = [b % 10 - a % 10 for a, b in pairwise(numbers)]

        seen_patterns = set()
        for i in range(len(numbers) - 4):
            pattern = tuple(differences[i:i + 4])
            if pattern not in seen_patterns:
                patterns[pattern] += numbers[i + 4] % 10
                seen_patterns.add(pattern)

    return max(patterns.values())


with open(filename, "r") as f_inp:
    initial_values = list(map(int, f_inp.read().splitlines()))
    print(simulate_first_phase(initial_values))
    print(simulate_second_phase(initial_values))

# filename = "test-data.txt"
filename = "data.txt"


def check_safe(levels):
    return levels in [sorted(levels), sorted(levels, reverse=True)] and all(
        1 <= abs(a - b) <= 3 for a, b in zip(levels, levels[1:])
    )


def check_safe_2(levels):
    return check_safe(levels) or any(
        check_safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels))
    )


with open(filename) as f:
    reports = [list(map(int, entry.split())) for entry in f.read().splitlines()]
    print(sum(check_safe(report) for report in reports))
    print(sum(check_safe_2(report) for report in reports))

# filename = "test-data.txt"

filename = "data.txt"

with open(filename) as f:
    entries = [list(map(int, line.split())) for line in f]
first, second = zip(*entries)
print(sum(abs(a - b) for a, b in zip(sorted(first), sorted(second))))
print(sum(a * second.count(a) for a in first))

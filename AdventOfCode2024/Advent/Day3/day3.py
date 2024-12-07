import re

# filename = "test-data.txt"


filename = "data.txt"


def get_all_mul(text):
    return sum(int(a) * int(b) for a, b in re.findall(r'mul\((-?\d+),(-?\d+)\)', text))


def get_enabled_all_mul(text):
    all_matches = re.findall(r"mul\((-?\d*),(-?\d*)\)|(do\(\))|(don't\(\))", text)
    total, enabled = 0, True
    for match in all_matches:
        if "do()" in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        else:
            if enabled:
                total += int(match[0]) * int(match[1])
    return total


with open(filename) as f_inp:
    text_data = f_inp.read()
    print(get_all_mul(text_data))
    print(get_enabled_all_mul(text_data))

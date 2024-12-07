# filename = "test-data.txt"


filename = "data.txt"


def is_update_valid(rules, update):
    return all(update.index(a) <= update.index(b) for a, b in rules if a in update and b in update)


def get_middle_correct(rules, updates):
    return sum(update[len(update) // 2] for update in updates if is_update_valid(rules, update))


def correct_update(rules, update):
    while not is_update_valid(rules, update):
        for first, second in rules:
            if first in update and second in update and update.index(first) > update.index(second):
                first_index, second_index = update.index(first), update.index(second)
                update[first_index], update[second_index] = update[second_index], update[first_index]


def get_middle_wrong(rules, updates):
    return sum(update[len(update) // 2] for update in updates if
               not is_update_valid(rules, update) and correct_update(rules, update) is None)


with open(filename) as f_inp:
    f_rules, f_updates = f_inp.read().split('\n\n')
    rules_data = [tuple(map(int, line.split("|"))) for line in f_rules.split('\n')]
    updates_data = [list(map(int, [entry for entry in line.split(",")])) for line in f_updates.split("\n")]
    print(get_middle_correct(rules_data, updates_data))
    print(get_middle_wrong(rules_data, updates_data))

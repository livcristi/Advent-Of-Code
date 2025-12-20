from functools import reduce
from typing import List, Tuple, Any
from z3 import Optimize, Bool, Int, Xor, If, Sum

raw_data: List[List[str]] = [
    line.strip().split(" ") for line in open("input.txt").readlines()
]

wanted_lights: List[List[bool]] = [
    [char == "#" for char in line[0].strip("[]")] for line in raw_data
]

possible_buttons: List[List[Tuple[int, ...]]] = [
    [tuple(map(int, btn.strip("()").split(","))) for btn in line[1:-1]]
    for line in raw_data
]

joltage_req: List[List[int]] = [
    list(map(int, line[-1].strip("{}").split(","))) for line in raw_data
]


def solve_lights(targets: List[bool], button_configs: List[Tuple[int, ...]]) -> int:
    solver: Optimize = Optimize()

    # We map each possible press as a binary variable
    presses: List[Any] = [Bool(f"p_{i}") for i in range(len(button_configs))]

    # Then we enforce constraints for each target light (basically -> XOR the input buttons that will light it up, so that it matches its desired value)
    for i, target_val in enumerate(targets):
        active_buttons: List[Any] = [
            presses[j] for j, config in enumerate(button_configs) if i in config
        ]
        if active_buttons:
            solver.add(reduce(Xor, active_buttons) == target_val)

    # We now find the minimum number of button presses and return that
    solver.minimize(Sum([If(p, 1, 0) for p in presses]))
    solver.check()

    return sum(1 for p in presses if solver.model().evaluate(p, model_completion=True))


def solve_joltages(targets: List[int], button_configs: List[Tuple[int, ...]]) -> int:
    solver: Optimize = Optimize()

    # We map each possible press as an int variable
    presses: List[Any] = [Int(f"p_{i}") for i in range(len(button_configs))]

    for p in presses:
        solver.add(p >= 0)

    # Then we enforce constraints for each target (basically -> SUM the input buttons that will light it up, so that it matches its desired value)
    for i, target_val in enumerate(targets):
        active_buttons: List[Any] = [
            presses[j] for j, config in enumerate(button_configs) if i in config
        ]
        if active_buttons:
            solver.add(Sum(active_buttons) == target_val)

    # We now find the minimum number of button presses and return that
    solver.minimize(Sum(presses))
    solver.check()

    return sum(solver.model().evaluate(p).as_long() for p in presses)


total_lights: int = sum(
    solve_lights(l, b) for l, b in zip(wanted_lights, possible_buttons)
)
total_joltages: int = sum(
    solve_joltages(j, b) for j, b in zip(joltage_req, possible_buttons)
)

print(total_lights, total_joltages)

import re

from z3 import BitVec, Optimize

# filename = "test-data.txt"


filename = "data.txt"


def combo_value(registers, operand):
    if 0 <= operand <= 3 or operand == 7:
        return operand
    return registers[operand - 4]


def process_program(registers, program, debug=True):
    ip = 0
    output = []
    while ip < len(program):
        instruction = program[ip]
        operand = program[ip + 1]
        if instruction == 0:
            registers[0] = registers[0] // (2 ** combo_value(registers, operand))
        elif instruction == 1:
            registers[1] = registers[1] ^ operand
        elif instruction == 2:
            registers[1] = combo_value(registers, operand) % 8
        elif instruction == 3:
            if registers[0] != 0:
                ip = operand
                continue
        elif instruction == 4:
            registers[1] = registers[1] ^ registers[2]
        elif instruction == 5:
            output.append(combo_value(registers, operand) % 8)
        elif instruction == 6:
            registers[1] = registers[0] // (2 ** combo_value(registers, operand))
        else:
            registers[2] = registers[0] // (2 ** combo_value(registers, operand))
        ip += 2
    if debug:
        print(",".join(map(str, output)))
    return registers, output


def find_right_registers(registers, program):
    found_register = False
    register_value = 0
    while not found_register:
        registers[0] = register_value
        _, output = process_program(registers.copy(), program, debug=False)
        if program == output:
            return register_value
        register_value += 1


def dummy_program():
    a = 45483412

    while a != 0:
        tmp = ((a % 8) ^ 6 ^ (a // (2 ** ((a % 8) ^ 3))))
        a = a // (2 ** 3)
        print(tmp % 8, end=",")


def solve_part2(program):
    opt = Optimize()
    s = BitVec('s', 64)
    a, b, c = s, 0, 0
    for x in program:
        b = a % 8
        b ^= 3
        c = a >> b
        a >>= 3
        b ^= c
        b ^= 5
        opt.add((b % 8) == x)
    opt.add(a == 0)
    opt.minimize(s)
    assert str(opt.check()) == 'sat'
    return opt.model().eval(s)


with open(filename, "r") as f_inp:
    raw_data = f_inp.read()
    registers_data = list(map(int, re.findall(r"Register [A-Z]: ([0-9]+)", raw_data)))
    program_data = list(map(int, re.findall(r"Program: ([0-9,]+)", raw_data)[0].split(",")))
    process_program(registers_data, program_data)
    print(solve_part2(program_data))

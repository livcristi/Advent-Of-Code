from functools import lru_cache

# filename = "test-data.txt"


filename = "data.txt"


def simulate_system(gates, values, operators):
    @lru_cache(maxsize=None)
    def evaluate(operator):
        if operator in values:
            return values[operator]
        expr = gates[operator]
        operator1 = evaluate(expr[0])
        operation = expr[1]
        operator2 = evaluate(expr[2])
        if operation == "AND":
            return operator1 & operator2
        elif operation == "OR":
            return operator1 | operator2
        elif operation == "XOR":
            return operator1 ^ operator2

    digits = {}
    for operator in operators:
        if operator.startswith("z"):
            digits[int(operator[1:])] = evaluate(operator)

    total_result = 0
    for dig, val in digits.items():
        total_result += (1 << dig) * val

    return total_result


def helper(gates, values, operators):
    @lru_cache(maxsize=None)
    def evaluate(operator):
        if operator in values:
            return values[operator]
        expr = gates[operator]
        operator1 = evaluate(expr[0])
        operation = expr[1]
        operator2 = evaluate(expr[2])
        if operation == "AND":
            return operator1 & operator2
        elif operation == "OR":
            return operator1 | operator2
        elif operation == "XOR":
            return operator1 ^ operator2

    def get_bytes(start):
        digits = {}
        for operator in operators:
            if operator.startswith(start):
                digits[int(operator[1:])] = evaluate(operator)
        for index in range(45, -1, -1):
            if index in digits:
                print(digits[index], end="")
            else:
                print(0, end="")
        print()

    def get_value(start):
        digits = {}
        for operator in operators:
            if operator.startswith(start):
                digits[int(operator[1:])] = evaluate(operator)
        total = 0
        for index in range(45, -1, -1):
            if index in digits:
                total += (1 << index) * digits[index]
        return total

    get_bytes("x")
    get_bytes("y")
    get_bytes("z")
    print(get_value("z"))
    print(bin(get_value("z")))
    print(bin(get_value("x") + get_value("y")))

    @lru_cache(maxsize=None)
    def inspect(op, depth=0):
        if op in values or depth >= 5:
            return op

        op1 = inspect(gates[op][0], depth + 1)
        op2 = inspect(gates[op][2], depth + 1)
        if gates[op][1] == "AND":
            return f"{op}{{({op1}) & ({op2})}}"
        if gates[op][1] == "OR":
            return f"{op}{{({op1}) | ({op2})}}"
        if gates[op][1] == "XOR":
            return f"{op}{{({op1}) ^ ({op2})}}"

    # Code I used to figure out how bit 7 was wrong:
    print(inspect("z00"))
    print(inspect("z01"))
    print(inspect("z02"))
    print(inspect("z03"))
    print(inspect("z04"))
    print(inspect("z05"))
    print(inspect("z06"))
    print(inspect("z07"))
    print(inspect("z08"))
    print(inspect("z09"))

    print("\n")
    # Code I used to figure out how bit 13 was wrong:
    print(inspect("z10"))
    print(inspect("z11"))
    print(inspect("z12"))
    print(inspect("z13"))
    print(inspect("z14"))
    print(inspect("z15"))
    print(inspect("z16"))
    print(evaluate("rbk"))
    print(evaluate("pmv"))
    print(evaluate("rbk"))
    print("\n")

    # Code I used to figure out how bit 18 was wrong:
    print(inspect("z16"))
    print(inspect("z17"))
    print(inspect("z18"))
    print(inspect("z19"))
    print(inspect("z20"))

    # Code I used to figure out how bit 26 was wrong:
    print(inspect("z22"))
    print(inspect("z23"))
    print(inspect("z24"))
    print(inspect("z25"))
    print(inspect("z26"))
    print(inspect("z27"))
    print(inspect("z28"))
    print(inspect("z29"))
    print(inspect("z30"))
    print(evaluate("z26"))
    print(evaluate("qkf"))
    print(evaluate("wkr"))
    # kvp OR qsm -> qkf
    print(evaluate("kvp"))
    print(evaluate("qsm"))


"""
0111101110101000100001111111001110010110100011 +  (33990941402531)
0101001010111001000011100001101111111011001101 =  (22738689785549)
1100111001100001100101011111111100001111110000    (56729630917616)
1100111001100001100101100000111110010001110000    (56729631188080) true


wrong bits: <7>, <13>, <18>, <26>
"""

with open(filename, "r") as f:
    values_data, gates_data = f.read().split("\n\n")
    gates = {}
    values = {}
    operators = set()
    for row in values_data.split("\n"):
        name, value = row.split(":")
        values[name.strip()] = int(value)
        operators.add(name.strip())

    # # HELPEEEEEEEEEEEER
    # for key, value in values.items():
    #     if key.startswith("x") or key.startswith("y"):
    #         values[key] = 1

    for row in gates_data.split("\n"):
        op1, opr, op2, _, res = row.split(" ")
        gates[res.strip()] = (op1.strip(), opr.strip(), op2.strip())
        operators.add(res.strip())
    # print(simulate_system(gates, values, operators))
    helper(gates, values, operators)

from itertools import chain, zip_longest

# filename = "test-data.txt"


filename = "data.txt"


def get_operators_from_hash_add_mult(operator_hash: int, length: int) -> list[str]:
    operators = []
    while operator_hash > 0:
        if operator_hash % 2 == 0:
            operators.append("+")
        else:
            operators.append("*")
        operator_hash //= 2
    operators.extend("+" * (length - len(operators)))
    return operators


def get_operators_from_hash_add_mult_conc(operator_hash: int, length: int) -> list[str]:
    operators = []
    while operator_hash > 0:
        if operator_hash % 3 == 0:
            operators.append("+")
        elif operator_hash % 3 == 1:
            operators.append("*")
        else:
            operators.append("||")
        operator_hash //= 3
    operators.extend("+" * (length - len(operators)))
    return operators


def get_equation_from_operands_and_operators(
    operands: list[int], operators: list[str]
) -> str:
    return [
        str(x)
        for x in chain.from_iterable(zip_longest(operands, operators))
        if x is not None
    ]


def evaluate_expression(expression: list[str]) -> int:
    while len(expression) > 1:
        value1 = expression.pop(0)
        operator = expression.pop(0)
        value2 = expression.pop(0)
        if "+" in operator:
            temp_result = int(value1) + int(value2)
        elif "*" in operator:
            temp_result = int(value1) * (int(value2))
        else:
            temp_result = int(value1 + value2)
        expression = [str(temp_result)] + expression
    return int(expression[0])


def is_equation_valid_add_mult(equation):
    result = equation[0]
    operands = equation[1]
    operators_count = len(operands) - 1
    for operators_hash in range(2 ** operators_count):
        operators = get_operators_from_hash_add_mult(operators_hash, operators_count)
        possible_equation = get_equation_from_operands_and_operators(
            operands, operators
        )
        if evaluate_expression(possible_equation) == result:
            return True
    return False


def is_equation_valid_add_mult_conc(equation):
    result = equation[0]
    operands = equation[1]
    operators_count = len(operands) - 1
    for operators_hash in range(3 ** operators_count):
        operators = get_operators_from_hash_add_mult_conc(
            operators_hash, operators_count
        )
        possible_equation = get_equation_from_operands_and_operators(
            operands, operators
        )
        if evaluate_expression(possible_equation) == result:
            return True
    return False


def get_total_correct_add_mult(equations):
    correct = 0
    for equation in equations:
        if is_equation_valid_add_mult(equation):
            correct += equation[0]
    return correct


def get_total_correct_add_mult_conc(equations):
    correct = 0
    for equation in equations:
        if is_equation_valid_add_mult_conc(equation):
            correct += equation[0]
    return correct


with open(filename, "r") as f_inp:
    equations_data = []
    for line in f_inp.readlines():
        line_result, line_operands = line.strip().split(":")
        line_result = int(line_result)
        line_operands = list(map(int, line_operands.split()))
        equations_data.append((line_result, line_operands))
    print(get_total_correct_add_mult(equations_data))
    print(get_total_correct_add_mult_conc(equations_data))

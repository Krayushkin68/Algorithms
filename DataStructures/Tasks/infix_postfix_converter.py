from DataStructures.stack import Stack


def infix_to_postfix(infixexpr):
    priority = {'*': 3,
                '/': 3,
                '+': 2,
                '-': 2,
                '(': 1}
    operators = Stack()
    result = []

    for el in infixexpr.split():
        if el not in '*/+-()':
            result.append(el)
        elif el == '(':
            operators.push(el)
        elif el == ')':
            top_el = operators.pop()
            while top_el != '(':
                result.append(top_el)
                top_el = operators.pop()
        elif el in '*/+-':
            while not operators.is_empty() and priority[operators.peek()] >= priority[el]:
                result.append(operators.pop())
            operators.push(el)

    while not operators.is_empty():
        result.append(operators.pop())

    return ' '.join(result)


def calculate(operator, a, b):
    a = float(a)
    b = float(b)

    if operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "+":
        return a + b
    elif operator == '-':
        return a - b
    else:
        raise Exception(f'Unknown operator "{operator}"')


def eval_postfix(postfixexpr):
    operands = Stack()
    for el in postfixexpr.split():
        if el not in '*/+-':
            operands.push(el)
        else:
            operand_b = operands.pop()
            operand_a = operands.pop()
            operands.push(calculate(el, operand_a, operand_b))
    return operands.pop()


def eval_infix(infix_expression):
    try:
        postfix_expression = infix_to_postfix(infix_expression)
        result = eval_postfix(postfix_expression)
        return result
    except Exception:
        return False


if __name__ == '__main__':
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    print(eval_postfix('7 8 + 3 2 + /'))
    print(eval_postfix('17 10 + 3 * 9 /'))

    print(eval_infix("10 + 3 * 5 / ( 16 - 4 )"))

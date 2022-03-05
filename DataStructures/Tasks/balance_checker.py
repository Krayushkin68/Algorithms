from DataStructures.stack import Stack


def balance_check(str_to_check):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()

    for el in str_to_check:
        if el in brackets.keys():
            stack.push(el)
        elif el in brackets.values():
            if brackets[stack.pop()] != el:
                return False
    else:
        return stack.size() == 0


if __name__ == '__main__':
    print(balance_check('{{([][])}()}'))
    print(balance_check('[{()]'))

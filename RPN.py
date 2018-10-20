
def RPN(rpn_str):
    ints = '1234567890'
    stack = []
    rpn_ls = list(rpn_str)
    while True:
        char = rpn_ls.pop(0)
        if char in ints:
            stack.append(char)

        elif char == '+':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(str(x + y))

        elif char == '-':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(str(x - y))

        elif char == '*':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(str(x * y))

        elif char == '%':
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(str(x % y))

        elif char == '=':
            return stack[-1]

from operator import add, sub, mul, truediv

ops = {'+': add, '-': sub, '*': mul, '/': truediv}

def calc(expr):
    stack = []
    for x in expr.split():
        if x in '+-*/':
            b, a = stack.pop(), stack.pop()
            x = ops[x](a, b)
        stack.append(float(x))
    return (stack or [0]).pop()


rpn_str = '123+-='

print(RPN(rpn_str))

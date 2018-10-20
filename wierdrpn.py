

def rpn(rpn_input):
    stack = []
    split_input = rpn_input.split()
    for object in split_input:
        stack += split_input.pop()
    return stack











rpn_input = '1 2 3 + *'
print(rpn(rpn_input))

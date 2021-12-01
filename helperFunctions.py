def parser(input_):
    lst = []
    for i in input_:
        lst.append(i)
    return lst


def precedence(i):
    # set precedence for arethmetic operators
    if i == '+' or i == '-':
        return 1
    elif i == '*' or i == '/':
        return 2
    elif i == '^':
        return 3
    else:
        return 0


def postfix_converter(infix):
    # convert infix to postfix
    postfix = []
    stack = []
    for i in infix:
        if i.isdigit():
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while len(stack) != 0 and precedence(i) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(i)
    while len(stack) != 0:
        postfix.append(stack.pop())
    return postfix



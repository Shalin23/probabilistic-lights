import additionTM
import multiplicationTM
import subtractionTM


def parser(input_):
    lst = []
    for i in input_:
        lst.append(i)
    return lst


def precedence(i):
    # set precedence for arithmetic operators
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
    print(infix)
    print("Boom:", infix.split(" "))
    postfix = []
    stack = []
    for i in infix.split(" "):
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


# evaluate postfix expression
def evaluate(infix):
    print('infix', infix)
    postfix = postfix_converter(infix)
    print('postfix', postfix)

    stack = []

    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(additionTM.turing_machine(str(1) * b + '+' + str(1) * a))
            elif i == '-':
                stack.append(subtractionTM.turing_machine((b * str(0)) + 'a' + (a * str(0))))
            elif i == '*':
                stack.append(multiplicationTM.turing_machine((b * str(1)) + '*' + (a * str(1))))
            elif i == '/':
                stack.append(str(1) * b / str(1) * a)
            elif i == '^':
                stack.append(str(1) * b ** str(1) * a)

    return stack.pop()

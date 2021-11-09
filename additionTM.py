def Transitions(current_state, tape_alpha):
    if current_state == 0:
        if tape_alpha == "0":
            return (1, "X", "R")
        elif tape_alpha == "a":
            return (3, "b", "R")

    elif current_state == 1:
        if tape_alpha == "0" or tape_alpha == "a":
            return (1, tape_alpha, "R")
        elif tape_alpha == "b":
            return (2, "0", "L")

    elif current_state == 2:
        if tape_alpha == "0" or tape_alpha == "a":
            return (2, tape_alpha, "L")  # return 0 or a
        elif tape_alpha == "X":
            return (0, "X", "R")


def input_parse(input_):
    lst = []
    for i in input_:
        lst.append(i)
    return lst


def TuringMachine(input):
    tape = []
    # current_tape = []  #null
    input_str = input_parse(input)
    for i in range(100):
        tape.append("b")
    tape = tape[:50] + input_str + tape[50:]
    # print(tape)

    i = 50
    current_state = 0
    direction = ""
    # current_state, tape[i], direction = Transitions(current_state,tape[i])  #x0 a 000 0
    if Transitions(current_state, tape[i]) == -1:
        print("not recognized ", i)
    else:
        current_state, tape[i], direction = Transitions(
            current_state, tape[i])  # x0 a 000 0
        while current_state != 3:

            if direction == "L":
                i = i-1
            elif direction == "R":
                i = i+1  # 53  54  55
            if Transitions(current_state, tape[i]) == None:
                print("not recognized ", i)
                break
            else:
                # print("lllll:", Transitions(current_state,tape[i]))
                current_state, tape[i], direction = Transitions(
                    current_state, tape[i])
        if current_state == 3:
            first_zero = tape.index("0")
            sum = 0

            while tape[first_zero] != "b":
                first_zero += 1
                sum += 1
            print(sum)


TuringMachine("000a0000")

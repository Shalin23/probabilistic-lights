import transitions
import inputParser


def turing_machine(input):
    tape = []
    # current_tape = []  #null
    input_str = inputParser.parser(input)
    for i in range(100):
        tape.append("b")
    tape = tape[:50] + input_str + tape[50:]
    # print(tape)
# TuringMachine("111+11")
    i = 50
    current_state = 0
    direction = ""
    # current_state, tape[i], direction = transitions.Transitions(current_state,tape[i])  #x0 a 000 0
    if transitions.Transitions(current_state, tape[i]) == -1:
        print("not recognized ", i)
    else:
        current_state, tape[i], direction = transitions.Transitions(
            current_state, tape[i])  # x0 a 000 0
        while current_state != 4:

            if direction == "L":
                i = i-1
            elif direction == "R":
                i = i+1  # 53  54  55
            if transitions.Transitions(current_state, tape[i]) == None:
                print("not recognized ", i)
                break
            else:
                # print("lllll:", transitions.Transitions(current_state,tape[i]))
                current_state, tape[i], direction = transitions.Transitions(
                    current_state, tape[i])
        if current_state == 4:
            first_zero = tape.index("0")
            sum = 0

            while tape[first_zero] != "b":
                first_zero += 1
                sum += 1
            print(f'The sum from Addition Turing Machine is {sum}')


# TuringMachine("000a0000")

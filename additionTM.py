import transitions
import helperFunctions

default_states = ["q_a", "q_r"]


# turing machine to read a tape and add the numbers on the tape
def turing_machine(input_str):
    # Define the states for the Turing Machine
    states = default_states.copy()
    for i in range(10):
        states.append("q" + str(i))

    # print("States: ", states)
    # print()

    tape = helperFunctions.parser(input_str) + ["#" for i in range(1000)]

    current_state = states[2]

    result = 0
    i = 0

    # create the turing machine
    while current_state not in default_states:
        if current_state not in default_states:
            operation = transitions.add(current_state, tape[i])

            current_state = operation[0]
            tape[i] = operation[1]

            if current_state in default_states:
                if current_state == "q_r":
                    print("Unable to process INPUT")
                    print()
                    return
            if operation[2] == "R":
                i += 1
            elif operation[2] == "L":
                i -= 1
            # print(tape)

    for i in tape:
        if i == "1":
            result += 1

    # print(f'The Turing Machine returned {result} by addition')
    return result


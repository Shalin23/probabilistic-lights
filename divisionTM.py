import transitions
import helperFunctions

default_states = ["q_a", "q_r"]


# turing machine to read a tape and multiply the numbers on the tape
# the tape is read from left to right, with the denominator being on the left
def turing_machine(input_str):
    print(input_str)
    # Define the states for the Turing Machine
    states = default_states.copy()
    for i in range(11):
        states.append("q" + str(i))

    # print("States: ", states)
    # print()

    tape = (
        ["#" for i in range(2)]
        + helperFunctions.parser(input_str)
        + ["#" for i in range(10)]
    )

    current_state = states[2]

    # steps = 0
    result = 0
    i = 0

    # create the turing machine
    while current_state not in default_states:
        steps += 1
        # print("Step: ", steps)
        # print("***** Pre-operation i = ", i)
        # print()

        # print("Current State: ", current_state)
        # print(current_state in default_states)
        # print()

        if current_state not in default_states:
            # print("--------------------")
            # print("Current State: ", current_state)
            # print("Current Head: ", tape[i])
            # print("--------------------")
            # print()

            operation = transitions.divide(current_state, tape[i])
            # print(">>>Operation: ", operation)
            # print()

            current_state = operation[0]
            tape[i] = operation[1]

            # print("Next State: ", current_state)
            # print("Tape: ", tape)
            # print()

            # print("Pre-operation i = ", i)

            if current_state in default_states:
                if current_state == "q_r":
                    print("Unable to process INPUT")
                    print()
                    return

            if operation[2] == "R":
                # print("Move right")
                i += 1
            elif operation[2] == "L":
                # print("Move left")
                i -= 1

            # print("Post-operation i = ", i)
            # print("------------------------------------------------------------")
            # print()

    for i in tape:
        if i == "1":
            result += 1

    # print(f'The Turing Machine returned {result} by multiplication')
    return result

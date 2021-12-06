import transitions
import helperFunctions

default_states = ["q_a", "q_r"]


# turing machine to read a tape and add the numbers on the tape
def turing_machine(input_str):
    print(f"Calculating {input_str} using the Addition Turing Machine")
    # Define the states for the Turing Machine
    states = default_states.copy()
    for i in range(10):
        states.append("q" + str(i))

    # print("States: ", states)
    # print()

    tape = helperFunctions.parser(input_str) + ["#" for i in range(10)] # increase range for larger computations

    current_state = states[2]

    result = 0
    i = 0

    # create the turing machine
    while current_state not in default_states:
        # steps += 1
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

            operation = transitions.add(current_state, tape[i])
            # print(">>>Operation: ", operation)
            # print()

            current_state = operation[0]
            tape[i] = operation[1]

            # print("Next State: ", current_state)
            print("Tape: ", tape)
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

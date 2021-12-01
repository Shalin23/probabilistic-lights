import transitions
import helperFunctions


def turing_machine(input_str):
    tape = []
    input_str = helperFunctions.parser(input_str)

    for i in range(100):
        tape.append("b")
    tape = tape[:50] + input_str + tape[50:]

    i = 49
    current_state = 0

    if transitions.subtract(current_state, tape[i]) == -1:
        print("String Rejected")
    else:
        current_state, tape[i], direction = transitions.subtract(current_state, tape[i])
        while current_state != 8:

            if direction == "L":
                i -= 1
            elif direction == "R":
                i += 1
            if transitions.subtract(current_state, tape[i]) is None:
                print("String Rejected")
                break
            else:
                current_state, tape[i], direction = transitions.subtract(current_state, tape[i])

        if current_state == 8 and "0" in tape:
            word = ""
            sum = 0
            if "-" in tape:
                word += "-"
            j = tape.index("0")

            while tape[j] != "b":
                sum += 1
                j += 1
            # print(f'The result from Subtraction Turing Machine is {word }{sum}')
            return word + str(sum)
        else:
            # print(f'The result from Subtraction Turing Machine is {str(0)}')
            return str(0)

# turing_machine("0000a0000")  # 0 (m==n)
# turing_machine("00a0000")  # -2  (m<n)
# turing_machine("00000a0000")  # 1  (m>n)

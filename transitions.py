def add(current_state, tape_alpha):
    if current_state == 0:
        if tape_alpha == "0":
            return (1, "X", "R")
        elif tape_alpha == "a":
            return (4, "b", "R")

    elif current_state == 1:
        if tape_alpha == "0":
            return (1, "0", "R")
        elif tape_alpha == "a":
            return (2, "a", "R")

    elif current_state == 2:
        if tape_alpha == "0":
            return (2, "0", "R")
        elif tape_alpha == "b":
            return (3, "0", "L")

    elif current_state == 3:
        if tape_alpha == "0" or tape_alpha == "a":
            return (3, tape_alpha, "L")  # return 0 or a
        elif tape_alpha == "X":
            return (0, "X", "R")


def subtract(current_state, tape_alpha):
    if current_state == 0:
        if tape_alpha == "0":
            return (1, "X", "R")
        elif tape_alpha == "a":
            return (4, "a", "R")

    elif current_state == 1:
        if tape_alpha == "0" or tape_alpha == "a":
            return (1, tape_alpha, "R")
        elif tape_alpha == "b":
            return (2, tape_alpha, "L")

    elif current_state == 2:
        if tape_alpha == "0":
            return (3, "b", "L")
        elif tape_alpha == "a":
            return (6, "0", "R")

    elif current_state == 3:
        if tape_alpha == "0" or tape_alpha == "a":
            return (3, tape_alpha, "L")
        elif tape_alpha == "X":
            return (0, tape_alpha, "R")

    elif current_state == 4:
        if tape_alpha == "0":
            return (5, tape_alpha, "L")

    elif current_state == 5:
        if tape_alpha == "a":
            return (6, "-", "R")


def multiply(current_state, head):
    # Dictionary of states and their transitions
    states_operations = {
        "q0": {
            "#": ("q0", "#", "R"),
            "*": ("q9", "#", "R"),
            "1": ("q1", "#", "R"),
        },
        "q1": {
            "*": ("q2", "*", "R"),
            "1": ("q1", "1", "R"),
        },
        "q2": {
            "#": ("q7", "#", "L"),
            "1": ("q3", "X", "R"),
        },
        "q3": {
            "#": ("q4", "#", "R"),
            "1": ("q3", "1", "R"),
        },
        "q4": {
            "#": ("q5", "1", "L"),
            "1": ("q4", "1", "R"),
        },
        "q5": {
            "#": ("q6", "#", "L"),
            "1": ("q5", "1", "L"),
        },
        "q6": {
            "X": ("q2", "X", "R"),
            "1": ("q6", "1", "L"),
        },
        "q7": {
            "X": ("q7", "1", "L"),
            "*": ("q8", "*", "L"),
        },
        "q8": {
            "#": ("q0", "#", "R"),
            "1": ("q8", "1", "L"),
        },
        "q9": {
            "#": ("q_a", "#", "R"),
            "1": ("q9", "#", "R"),
        },
        "q_a": "ACCEPTED",
        "q_r": "REJECTED",
    }

    return states_operations[current_state][head]

def add(current_state, head):
    # Dictionary of states and their transitions
    states_operations = {
        "q0": {
            "#": ("q0", "#", "R"),
            "+": ("q_a", "#", "R"),
            "1": ("q1", "X", "R"),
        },
        "q1": {
            "+": ("q2", "+", "R"),
            "1": ("q1", "1", "R"),
        },
        "q2": {
            "#": ("q3", "#", "L"),
            "1": ("q2", "1", "R"),
        },
        "q3": {
            "+": ("q4", "+", "L"),
            "1": ("q3", "1", "L"),
        },
        "q4": {
            "X": ("q5", "X", "R"),
            "1": ("q4", "1", "L"),
        },
        "q_a": ("q_a", "q_a", "ACCEPTED"),
        "q_r": ("q_r", "q_r", "REJECTED"),
    }
    if head not in states_operations[current_state]:
        return states_operations["q_r"]

    return states_operations[current_state][head]


def subtract(current_state, tape_alpha):
    if current_state == 0:
        if tape_alpha == "b":
            return(1, "b", "R")
    if current_state == 1:
        if tape_alpha == "0":
            return (2, "X", "R")
        elif tape_alpha == "a":
            return (5, "a", "R")

    elif current_state == 2:
        if tape_alpha == "0" or tape_alpha == "a":
            return (2, tape_alpha, "R")
        elif tape_alpha == "b":
            return (3, tape_alpha, "L")

    elif current_state == 3:
        if tape_alpha == "0":
            return (4, "b", "L")
        elif tape_alpha == "a":
            return (8, "0", "R")

    elif current_state == 4:
        if tape_alpha == "0" or tape_alpha == "a":
            return (4, tape_alpha, "L")
        elif tape_alpha == "X":
            return (1, tape_alpha, "R")

    elif current_state == 5:
        if tape_alpha == "0":
            return (6, tape_alpha, "L")
        if tape_alpha == "b":
            return (8, tape_alpha, "L")

    elif current_state == 6:
        if tape_alpha == "a":
            return (8, "-", "R")

    elif current_state == 7:
        if tape_alpha == "a":
            return (8, "X", "R")


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
        "q_a": ("q_a", "q_a", "ACCEPTED"),
        "q_r": ("q_r", "q_r", "REJECTED"),
    }

    if head not in states_operations[current_state]:
        return states_operations["q_r"]

    return states_operations[current_state][head]

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
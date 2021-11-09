def Transitions(current_state, tape_alpha):
    if current_state == 0:
        if tape_alpha == "0":
            return (1, "X", "R")
        elif tape_alpha == "a":
            return (4, "a", "R")

    elif current_state == 1:
        if tape_alpha == "0" or tape_alpha == "a":
            return (1, tape_alpha, "R")
        elif tape_alpha == "b":
            return (2, tape_alpha , "L")

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
    
    

def input_parse(input_):
    lst = []
    for i in input_:
        lst.append(i)
    return lst


def TuringMachine(input):

    tape = []
    input_str = input_parse(input)

    for i in range(100):
        tape.append("b")
    tape = tape[:50] + input_str + tape[50:]

    i = 50
    current_state = 0

    if Transitions(current_state, tape[i]) == -1:
        print("String Rejected")
    else:
        current_state, tape[i], direction = Transitions(current_state, tape[i])
        while current_state != 6:

            if direction == "L":
                i -= 1
            elif direction == "R":
                i += 1  
            if Transitions(current_state, tape[i]) == None:
                print("String Rejected")
                break
            else:
                current_state, tape[i], direction = Transitions(current_state, tape[i])
        
        if current_state == 6:
            word = "" 
            sum = 0  
            if "-" in tape:
                word += "-"   
            j = tape.index("0")
            
            while tape[j] != "b":
                sum += 1
                j += 1
            print(word + str(sum))
            

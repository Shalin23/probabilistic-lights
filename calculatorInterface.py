from tkinter import *
import helperFunctions

expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equal_press():
    try:
        global expression
        print("expression:", expression)
        if "/" in expression:
            equation.set(eval(expression))
            expression = ""
            return
        else:
            total = helperFunctions.evaluate(expression)

        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


gui = Tk()

# set the background colour of GUI window
gui.configure(background="#063341")

# set the title of GUI window
gui.title("Turing Calculator")

# set the configuration of GUI window
gui.geometry("170x235")

equation = StringVar()

expression_field = Entry(
    gui,
    textvariable=equation,
    width=11,
    fg="#EF476F",
    bg="#073B4C",
    font="'sans 8 bold",
)
expression_field.grid(columnspan=4, ipadx=50, ipady=10)

button0 = Button(
    gui,
    text=" 0 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(0),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button0.grid(row=5, column=1)

button1 = Button(
    gui,
    text=" 1 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(1),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button1.grid(row=4, column=0)

button2 = Button(
    gui,
    text=" 2 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(2),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button2.grid(row=4, column=1)

button3 = Button(
    gui,
    text=" 3 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(3),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button3.grid(row=4, column=2)

button4 = Button(
    gui,
    text=" 4 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(4),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button4.grid(row=3, column=0)

button5 = Button(
    gui,
    text=" 5 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(5),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button5.grid(row=3, column=1)

button6 = Button(
    gui,
    text=" 6 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(6),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button6.grid(row=3, column=2)

button7 = Button(
    gui,
    text=" 7 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(7),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button7.grid(row=2, column=0)

button8 = Button(
    gui,
    text=" 8 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(8),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button8.grid(row=2, column=1)

button9 = Button(
    gui,
    text=" 9 ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(9),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
button9.grid(row=2, column=2)

plus = Button(
    gui,
    text=" + ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(" + "),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
plus.grid(row=1, column=3)

minus = Button(
    gui,
    text=" - ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(" - "),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
minus.grid(row=2, column=3)

multiply = Button(
    gui,
    text=" × ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(" * "),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
multiply.grid(row=3, column=3)

divide = Button(
    gui,
    text=" ÷ ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(" / "),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
divide.grid(row=4, column=3)

open_bracket = Button(
    gui,
    text=" ( ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press("( "),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
open_bracket.grid(row=1, column=1)

close_bracket = Button(
    gui,
    text=" ) ",
    fg="#EF476F",
    bg="#063341",
    command=lambda: press(" )"),
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
close_bracket.grid(row=1, column=2)

equal = Button(
    gui,
    text=" = ",
    fg="#063341",
    bg="#EF476F",
    command=equal_press,
    height=2,
    width=10,
    font="'sans 8 bold",
)
equal.grid(row=5, column=2, columnspan=2)

clear = Button(
    gui,
    text="CE",
    fg="#EF476F",
    bg="#063341",
    command=clear,
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
clear.grid(row=1, column=0)

blank1 = Button(
    gui,
    text="",
    fg="#EF476F",
    bg="#063341",
    height=2,
    width=4,
    activebackground="#EF476F",
    font="'sans 8 bold",
)
blank1.grid(row=5, column=0)

# blank2 = Button(
#     gui,
#     text="",
#     fg="#EF476F",
#     bg="#063341",
#     height=2,
#     width=4, activebackground="#EF476F",
#     font="'sans 8 bold",
# )
# blank2.grid(row=5, column=3)

# start the GUI
gui.mainloop()

# Calculator using python
# Using python tkinter module

from tkinter import *

solution = ""


# function for updating solution


def press(num):
    global solution
    solution += str(num)

    # update using set
    equation.set(solution)


def equalkey():
    try:

        global solution

        total = str(eval(solution))

        equation.set(total)

        # empty solution for initialize
        solution = ""

    # for error

    except:

        equation.set("Error")
        solution = ""


# for clear

def clear():
    global solution
    solution = ""
    equation.set("")

# Driver code


if __name__ == '__main__':
    # create a gui windows
    gui = Tk()

    # set the title
    gui.title("Calculator")

    # size of gui window
    gui.geometry("285x130")

    equation = StringVar()

    # Entry box
    solution_space = Entry(gui, textvariable=equation)
    solution_space.grid(columnspan=4, ipadx=80)

    # Create Buttons

    button1 = Button(gui, text='1', command=lambda: press(1), height=1, width=8)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text='2', command=lambda: press(2), height=1, width=8)
    button2.grid(row=2, column=1)
    button3 = Button(gui, text='3', command=lambda: press(3), height=1, width=8)
    button3.grid(row=2, column=2)
    button4 = Button(gui, text='4', command=lambda: press(4), height=1, width=8)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text='5', command=lambda: press(5), height=1, width=8)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text='6', command=lambda: press(6), height=1, width=8)
    button6.grid(row=3, column=2)
    button7 = Button(gui, text='7', command=lambda: press(7), height=1, width=8)
    button7.grid(row=4, column=0)
    button8 = Button(gui, text='8', command=lambda: press(8), height=1, width=8)
    button8.grid(row=4, column=1)
    button9 = Button(gui, text='9', command=lambda: press(9), height=1, width=8)
    button9.grid(row=4, column=2)
    button0 = Button(gui, text='0', command=lambda: press(0), height=1, width=8)
    button0.grid(row=5, column=0)

    # operator buttons
    plus = Button(gui, text=' + ', command=lambda: press("+"), height=1, width=8)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ',  command=lambda: press("-"), height=1, width=8)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', command=lambda: press("*"), height=1, width=8)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', command=lambda: press("/"), height=1, width=8)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', command=equalkey, height=1, width=8)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', command=clear, height=1, width=8)
    clear.grid(row=5, column=1)

    Decimal = Button(gui, text='.', command=lambda: press('.'), height=1, width=8)

    gui.mainloop()

    
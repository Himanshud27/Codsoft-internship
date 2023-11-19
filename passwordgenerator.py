# Python program for generating random password using Tkinter module

import random
from tkinter import *
from tkinter.ttk import *   # for combobox


def val():
    entry.delete(0, END)

    length = var1.get()

    # data of password

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    # strength selected is strong
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password

    # strength selected is medium
    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(uppercase)
        return password

    # strength selected is low

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(lowercase)
        return password

    else:
        print("Please choose an option")

# for generating passwords


def generate():
    password1 = val()
    entry.insert(10, password1)


# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title(" Password Generator")

# create label and entry to show

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)


c_label = Label(root, text="Length")
c_label.grid(row=1)


# Button that will generate the password
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio Buttons for deciding the
# strength of password

radio_low = Radiobutton(root, text="Low", variable=var, value=3)
radio_low.grid(row=1, column=2, )
radio_middle = Radiobutton(root, text="Medium", variable=var, value=2)
radio_middle.grid(row=1, column=3, )
radio_strong = Radiobutton(root, text="Strong", variable=var, value=1)
radio_strong.grid(row=1, column=4, )
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 12, 18, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)


root.mainloop()

from tkinter import *

# Empty data

data = []

# Add data in contact list


def add():
    global data
    data.append([Name.get(), Number.get(), Address.get(1.0, "end-1c")])
    update_book()


# Show data


def show():
    Name.set(data[int(select.curselection()[0])][0])
    Number.set(data[int(select.curselection()[0])][1])
    Address.delete(1.0, "end")
    Address.insert(1.0, data[int(select.curselection()[0])][2])

# delete data


def delete():
    del data[int(select.curselection()[0])]
    update_book()

# Reset the data


def reset():
    Name.set('')
    Number.set('')
    Address.delete(1.0, "end")


# Update the contact list
def update_book():
    select.delete(0, END)
    for n, p, a in data:
        select.insert(END, n)


if __name__ == '__main__':

    # creating gui window
    root = Tk()

    # window size
    root.geometry("500x500")

    root.title("Contact Book")

    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=20)

    Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable=Name, width=50).pack()

    Label(frame1, text='Phone No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable=Number, width=50).pack()

    Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
    Address = Text(frame2, width=50, height=10)
    Address.pack()

    Button(root, text="Add", font="arial 12 bold", command=add).place(x=100, y=270, width=50)
    Button(root, text="View", font="arial 12 bold", command=show).place(x=100, y=310, width=50)
    Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=350, width=50)
    Button(root, text="Reset", font="arial 12 bold", command=reset).place(x=100, y=390, width=50)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200, y=260)

    root.mainloop()

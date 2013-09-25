import sys
from Tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
var = StringVar()
label = Entry( frame, textvar=var, relief=RAISED, bg = "white", fg = "black")
var.set("0")
a = "0"
label.pack(side = RIGHT)
def num_0():
    global a
    if a == "0":
        a = "0"
    else:
        a += "0"
    var.set(a)
def num_1():
    global a
    if a == "0":
        a = "1"
    else:
        a += "1"
    var.set(a)
def num_2():
    global a
    if a == "0":
        a = "2"
    else:
        a += "2"
    var.set(a)
def num_3():
    global a
    if a == "0":
        a = "3"
    else:
        a += "3"
    var.set(a)
def num_4():
    global a
    if a == "0":
        a = "4"
    else:
        a += "4"
    var.set(a)
def num_5():
    global a
    if a == "0":
        a = "5"
    else:
        a += "5"
    var.set(a)
def num_6():
    global a
    if a == "0":
        a = "6"
    else:
        a += "6"
    var.set(a)
def num_7():
    global a
    if a == "0":
        a = "7"
    else:
        a += "7"
    var.set(a)
def num_8():
    global a
    if a == "0":
        a = "8"
    else:
        a += "8"
    var.set(a)
def num_9():
    global a
    if a == "0":
        a = "9"
    else:
        a += "9"
    var.set(a)
def plus():
    global a
    a += "+"
    var.set(a)
def subtract():
    global a
    a += "-"
    var.set(a)
def dot():
    global a
    a += "."
    var.set(a)
def multiply():
    global a
    a += "*"
    var.set(a)
def divide():
    global a
    a += "/"
    var.set(a)
def modulo():
    global a
    a += "%"
    var.set(a)
def clear():
    global a
    a = "0"
    var.set(a)
def back():
    global a
    a = a[:-1]
    if len(a) == 0:
        a = "0"
    var.set(a)
def equals():
    global a
    a = str(eval(a))
    var.set(a)
frame_1 = Frame(root)
frame_1.pack( side = BOTTOM )
minus = Button(frame_1, text = "(-)", width = "1")
minus.pack(side = LEFT)
zero = Button(frame_1, text = "0", width = "1", command = num_0)
zero.pack(side = LEFT)
dot = Button(frame_1, text = ".", width = "1", command = dot)
dot.pack(side = LEFT)
divide = Button(frame_1, text = "/", width = "1", command = divide)
divide.pack(side = LEFT)
equalto = Button(frame_1, text = "=", width = "1", command = equals)
equalto.pack(side = LEFT)
frame_2 = Frame(root)
frame_2.pack( side = BOTTOM )
one = Button(frame_2, text = "1", width = "1", command = num_1)
one.pack(side = LEFT)
two = Button(frame_2, text = "2", width = "1", command = num_2)
two.pack(side = LEFT)
three = Button(frame_2, text = "3", width = "1", command = num_3)
three.pack(side = LEFT)
multiply = Button(frame_2, text = "*", width = "1", command = multiply)
multiply.pack(side = LEFT)
percentage = Button(frame_2, text = "%", width = "1", command = modulo)
percentage.pack(side = LEFT)
frame_3 = Frame(root)
frame_3.pack( side = BOTTOM )
four = Button(frame_3, text = "4", width = "1", command = num_4)
four.pack(side = LEFT)
five = Button(frame_3, text = "5", width = "1", command = num_5)
five.pack(side = LEFT)
six = Button(frame_3, text = "6", width = "1", command = num_6)
six.pack(side = LEFT)
minus = Button(frame_3, text = "-", width = "1", command = subtract)
minus.pack(side = LEFT)
clear = Button(frame_3, text = "C", width = "1", command = clear)
clear.pack(side = LEFT)
frame_4 = Frame(root)
frame_4.pack( side = BOTTOM )
seven = Button(frame_4, text = "7", width = "1", command = num_7)
seven.pack(side = LEFT)
eight = Button(frame_4, text = "8", width = "1", command = num_8)
eight.pack(side = LEFT)
nine = Button(frame_4, text = "9", width = "1", command = num_9)
nine.pack(side = LEFT)
plus = Button(frame_4, text = "+", width = "1", command = plus)
plus.pack(side = LEFT)
remove = Button(frame_4, text = "<", width = "1", command = back)
remove.pack(side = LEFT)
root.mainloop()

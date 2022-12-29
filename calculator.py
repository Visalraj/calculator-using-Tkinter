from tkinter import *

window = Tk()
window.geometry("280x280")
window.title("Calculator")
expression = StringVar()
window.configure(background="#1C1C1C")
text = Entry(window, textvariable=expression, bg="white", fg="black", width="24", font=('Bold', 12), justify='right')
text.place(x=50, y=20, height=30)


# start of functions

def getvalue(item):
    global value
    value = str(value)
    value = value + str(item)

    expression.set(value)


def cleartext(item):
    global value
    global storedvalue
    global result
    value = ""
    storedvalue = ""
    result = ""
    expression.set(value)


def getoperation(item):
    global value
    global storedvalue
    global operationvariable
    storedvalue = int(value)
    value = ""
    expression.set(value)
    operationvariable = item


def equals(item):
    global result
    global storedvalue
    global value
    global operationvariable
    if operationvariable == "+":
        result = storedvalue + int(value)
        expression.set(result)
        value = result
    elif operationvariable == "-":
        result = storedvalue - int(value)
        expression.set(result)
        value = result
    elif operationvariable == "*":
        result = storedvalue * int(value)
        expression.set(result)
        value = result
    else:
        result = storedvalue / int(value)
        expression.set(result)
        value = result


value = ""
storedvalue = ""
result = ""
operationvariable = ""
# start of first row buttons

button1 = Button(text="7", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(7))
button2 = Button(text="8", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(8))
button3 = Button(text="9", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(9))
button4 = Button(text="X", bg="#FF9500", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getoperation("*"))
# end of first row buttons

# start of second row buttons
button5 = Button(text="4", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(4))
button6 = Button(text="5", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(5))
button7 = Button(text="6", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(6))
button8 = Button(text="-", bg="#FF9500", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getoperation("-"))
# end of second row buttons

# start of third row buttons
button9 = Button(text="1", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                 command=lambda: getvalue(1))
button10 = Button(text="2", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: getvalue(2))
button11 = Button(text="3", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: getvalue(3))
button12 = Button(text="+", bg="#FF9500", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: getoperation("+"))
# start of third row buttons

# start of fourth row buttons
button13 = Button(text="AC", bg="#D4D4D2", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: cleartext(""))
button14 = Button(text="0", bg="#505050", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: getvalue(0))
button15 = Button(text="/", bg="#FF9500", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: getoperation("/"))
button16 = Button(text="=", bg="#FF9500", fg="white", width="5", height="1", font=('SansSerif Bold', 13),
                  command=lambda: equals("="))
# start of fourth row buttons

# adding of first row buttons
button1.place(x=13, y=80)
button2.place(x=83, y=80)
button3.place(x=153, y=80)
button4.place(x=223, y=80)
# end of adding first row buttons

# adding of second row buttons
button5.place(x=13, y=125)
button6.place(x=83, y=125)
button7.place(x=153, y=125)
button8.place(x=223, y=125)
# end of adding  second row buttons

# adding of third row buttons
button9.place(x=13, y=170)
button10.place(x=83, y=170)
button11.place(x=153, y=170)
button12.place(x=223, y=170)
# end of adding of third row buttons

# adding of fourth row buttons
button13.place(x=13, y=220)
button14.place(x=83, y=220)
button15.place(x=153, y=220)
button16.place(x=223, y=220)
# end of adding of fourth row buttons


window.mainloop()

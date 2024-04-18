# Importing Tkinter
from tkinter import *

# Declaring the expression variable
expression = ""


# Function to update the expression
def press(num):

    global expression

    # Concatenation of string
    expression = expression + str(num)

    # Using set method to update the expression
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():

    # Using Try and Except to avoid error like 0 division
    try:
        global expression

        # Using eval and str to evaluate and convert the result into string
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    # Handling an error with the except block
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# Creating root window
calculator_app = Tk()
calculator_app.title("Calculator")

# calculator_app.configure(background='misty rose')

# Setting window width and height
calculator_app.geometry("300x500")

# Setting the entry box for showing the expression
equation = StringVar()
expression_field = Entry(calculator_app, textvariable=equation)
expression_field.grid(columnspan=5, ipadx=150, sticky="NSEW")
Font_tuple = ("Comic Sans MS", 20, "bold")
expression_field.configure(font=Font_tuple)


# Specifying grid
Grid.rowconfigure(calculator_app, 0, weight=1)
Grid.columnconfigure(calculator_app, 0, weight=1)
Grid.rowconfigure(calculator_app, 1, weight=1)
Grid.columnconfigure(calculator_app, 1, weight=1)
Grid.rowconfigure(calculator_app, 2, weight=1)
Grid.columnconfigure(calculator_app, 2, weight=1)
Grid.rowconfigure(calculator_app, 3, weight=1)
Grid.columnconfigure(calculator_app, 3, weight=1)
Grid.rowconfigure(calculator_app, 4, weight=1)
Grid.columnconfigure(calculator_app, 4, weight=1)

# Setting buttons font
Buttons_font = ("Comic Sans MS", 10, "bold")

# Creating buttons and locating them in particular place inside the root window
# Allowing the buttons to execute the given function or command
divide = Button(calculator_app, text="/", activebackground="deep sky blue",
                command=lambda: press("/"), heigh=5, width=5)
divide.grid(row=4, column=3, sticky="NSEW")
divide.configure(font=Buttons_font)

multiply = Button(calculator_app, text="*", activebackground="deep sky blue",
                  command=lambda: press("*"), heigh=5, width=5)
multiply.grid(row=3, column=3, sticky="NSEW")
multiply.configure(font=Buttons_font)

plus = Button(calculator_app, text="+", activebackground="deep sky blue",
              command=lambda: press("+"), heigh=5, width=5)
plus.grid(row=2, column=3, sticky="NSEW")
plus.configure(font=Buttons_font)

minus = Button(calculator_app, text="-", activebackground="deep sky blue",
               command=lambda: press("-"), heigh=5, width=5)
minus.grid(row=1, column=3, sticky="NSEW")
minus.configure(font=Buttons_font)

equal = Button(calculator_app, text=" = ", activebackground="deep sky blue",
               command=equalpress, heigh=5, width=5)
equal.grid(row=4, column=2, sticky="NSEW")
equal.configure(font=Buttons_font)

clear = Button(calculator_app, text="C", activebackground="deep sky blue",
               command=clear, heigh=5, width=5)
clear.grid(columnspan=1, rowspan=4, row=1, column=4, sticky="NSEW")
clear.configure(font=Buttons_font)

zero = Button(calculator_app, text="0", activebackground="deep sky blue",
              command=lambda: press(0), heigh=5, width=5)
zero.grid(row=4, column=0, sticky="NSEW")
zero.configure(font=Buttons_font)

one = Button(calculator_app, text="1", activebackground="deep sky blue",
             command=lambda: press(1), heigh=5, width=5)
one.grid(row=1, column=0, sticky="NSEW")
one.configure(font=Buttons_font)

two = Button(calculator_app, text="2", activebackground="deep sky blue",
             command=lambda: press(2), heigh=5, width=5)
two.grid(row=1, column=1, sticky="NSEW")
two.configure(font=Buttons_font)

three = Button(calculator_app, text="3", activebackground="deep sky blue",
               command=lambda: press(3), heigh=5, width=5)
three.grid(row=1, column=2, sticky="NSEW")
three.configure(font=Buttons_font)

four = Button(calculator_app, text="4", activebackground="deep sky blue",
              command=lambda: press(4), heigh=5, width=5)
four.grid(row=2, column=0, sticky="NSEW")
four.configure(font=Buttons_font)

five = Button(calculator_app, text="5", activebackground="deep sky blue",
              command=lambda: press(5), heigh=5, width=5)
five.grid(row=2, column=1, sticky="NSEW")
five.configure(font=Buttons_font)

six = Button(calculator_app, text="6", activebackground="deep sky blue",
             command=lambda: press(6), heigh=5, width=5)
six.grid(row=2, column=2, sticky="NSEW")
six.configure(font=Buttons_font)

seven = Button(calculator_app, text="7", activebackground="deep sky blue",
               command=lambda: press(7), heigh=5, width=5)
seven.grid(row=3, column=0, sticky="NSEW")
seven.configure(font=Buttons_font)

eight = Button(calculator_app, text="8", activebackground="deep sky blue",
               command=lambda: press(8), heigh=5, width=5)
eight.grid(row=3, column=1, sticky="NSEW")
eight.configure(font=Buttons_font)

nine = Button(calculator_app, text="9", activebackground="deep sky blue",
              command=lambda: press(9), heigh=5, width=5)
nine.grid(row=3, column=2, sticky="NSEW")
nine.configure(font=Buttons_font)

decimal = Button(calculator_app, text=".", activebackground="deep sky blue",
                 command=lambda: press("."), heigh=5, width=5)
decimal.grid(row=4, column=1, sticky="NSEW")
decimal.configure(font=Buttons_font)


# Running the app
calculator_app.mainloop()

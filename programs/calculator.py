from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os

def calculator_launch():
    sun_icon_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', 'sun.ico'))
    print(sun_icon_path)

    calc_window = Toplevel()
    calc_window.title('Simple Calculator')
    calc_window.iconbitmap(sun_icon_path)

    e = Entry(calc_window, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    #button functions

    #function for whenever a number or '.' is selected
    def button_click(number):
        #global variable to detect if = is pressed consecutive times
        global consecutive
        consecutive = False

        current = e.get()
        e.delete(0, END)
        #appending value in entry field
        e.insert(0, str(current) + str(number))

        print(consecutive)

    def button_clear():
        e.delete(0, END)

    def button_add():
        first_number = e.get()
        #global variable to hold first number being added
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        e.delete(0, END)

    def button_equal():
        global f_num
        global second_number
        #variables for consecutive = presses
        global consecutive
        global consecutive_base

        #pulls in second number input
        second_number = e.get()
        e.delete(0, END)

        print(f_num)
        print(second_number)
        print(consecutive)

        #if equals is NOT selected consecutive times
        if consecutive == False:
            #variable set to hold second value for consecutive = presses
            consecutive_base = second_number

            if math == "addition":
                e.insert(0, f_num + float(second_number))
            elif math == "subtraction":
                e.insert(0, f_num - float(second_number))
            elif math == "multiplication":
                e.insert(0, round(float(f_num) * float(second_number),2))
            elif math == "division":
                #checking divide by 0
                if second_number == 0:
                    messagebox.showerror("Error", "Can't Div By 0")
                    e.delete(0, END)
                else:
                    e.insert(0, round(float(f_num) / float(second_number), 2))
        else:
            #if consecutive presses, the "second_number" is used as the running total with "consecutive_base" used as the repeated modifier
            if math == "addition":
                e.insert(0, float(second_number) + float(consecutive_base))
            elif math == "subtraction":
                e.insert(0, float(second_number) - float(consecutive_base))
            elif math == "multiplication":
                e.insert(0, round(float(second_number) * float(consecutive_base),2))
            elif math == "division":
                e.insert(0, round(float(second_number) / float(consecutive_base), 2))

        consecutive = True

    def button_subtract():
        first_number = e.get()
        #global variables
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        e.delete(0, END)

    def button_multiply():
        first_number = e.get()
        #global variables
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        e.delete(0, END)

    def button_divide():
        first_number = e.get()
        #global variables
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        e.delete(0, END)

    # define num buttons

    button_1 = Button(calc_window, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(calc_window, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(calc_window, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(calc_window, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(calc_window, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(calc_window, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(calc_window, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(calc_window, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(calc_window, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(calc_window, text="0", padx=40, pady=20, command=lambda: button_click(0))

    button_dot = Button(calc_window, text=".", padx=42, pady=20, command=lambda: button_click('.'))

    button_add = Button(calc_window, text="+", padx=40, pady=20, command=button_add)
    button_equal = Button(calc_window, text="=", padx=138, pady=20, command=button_equal)
    button_clear = Button(calc_window, text="Clear", padx=129, pady=20, command=button_clear)

    button_subtract = Button(calc_window, text="-", padx=41, pady=20, command=button_subtract)
    button_multiply = Button(calc_window, text="*", padx=41, pady=20, command=button_multiply)
    button_divide = Button(calc_window, text="/", padx=41, pady=20, command=button_divide)

    # Put buttons on the screen

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_dot.grid(row=4, column=1)
    button_clear.grid(row=7, column=0, columnspan=3)
    button_add.grid(row=4, column=2)
    button_equal.grid(row=6, column=0, columnspan=3)

    button_subtract.grid(row=5, column=0)
    button_multiply.grid(row=5, column=1)
    button_divide.grid(row=5, column=2)
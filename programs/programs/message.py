from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os

def message_launch():
    sun_icon_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', 'sun.ico'))
    print(sun_icon_path)

    msg_window = Toplevel()
    msg_window.title('Message Demo')
    msg_window.iconbitmap(sun_icon_path)
    msg_window.geometry("300x425")

    MODES = [
        ("Show Info Msg", "show_info"),
        ("Show Warning Msg", "show_warning"),
        ("Show Error Msg", "show_error"),
        ("Ask Question Msg", "ask_question"),
        ("Ok or Cancel Msg", "ask_okcancel"),
        ("Yes or No Msg", "ask_yesno")
    ]

    #global declaration stops options from being mouse-over selected (weird bug)
    global msg_window_radio
    msg_window_radio = StringVar()
    #set to first option by default
    msg_window_radio.set("show_info")

    radio_label = Label(msg_window, text="Select an option radio buttons:", font="Verdana 10 bold").pack(pady = (5,0))

    #generating the radiobuttons w/ all the entries in modes
    for text, mode in MODES:
        Radiobutton(msg_window, text=text, variable=msg_window_radio, value=mode).pack(anchor='w', fill=BOTH)

    # syntax for different types of message boxes
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

    #function that checks then displays the selected type of message box
    def radio_popup(type):
        #response = messagebox.askyesno("This is my Popup!", "WTFFFFFFFFFFF")
        #Label(msg_window, text=response).pack()
        #print(type)

        if type == "show_info":
            response = messagebox.showinfo("This box shows info", "Look at all this info!")
        elif type == "show_warning":
            response = messagebox.showwarning("This box is a warning", "Warning!")
        elif type == "show_error":
            response = messagebox.showerror("This box is an error", "Error!")
        elif type == "ask_question":
            response = messagebox.askquestion("This box asks a question", "Do you like this question?")
        elif type == "ask_okcancel":
            response = messagebox.askokcancel("This box asks ok or cancel", "Ok or Cancel?")
        elif type == "ask_yesno":
            response = messagebox.askyesno("This box asks yes or no", "Yes or No?")

        #'response' is set depending on which type of window is selected, shows return values in the terminal
        print(response)
    Button(msg_window, text="Popup From Radio Options", command=lambda: radio_popup(msg_window_radio.get())).pack(pady=(10,0))


    #dropdown variables
    global msg_window_drop
    msg_window_drop = StringVar()
    msg_window_drop.set(MODES[0][0])

    def drop_popup(type):
        if type == "Show Info Msg":
            response = messagebox.showinfo("This box shows info", "Look at all this info!")
        elif type == "Show Warning Msg":
            response = messagebox.showwarning("This box is a warning", "Warning!")
        elif type == "Show Error Msg":
            response = messagebox.showerror("This box is an error", "Error!")
        elif type == "Ask Question Msg":
            response = messagebox.askquestion("This box asks a question", "Do you like this question?")
        elif type == "Ok or Cancel Msg":
            response = messagebox.askokcancel("This box asks ok or cancel", "Ok or Cancel?")
        elif type == "Yes or No Msg":
            response = messagebox.askyesno("This box asks yes or no", "Yes or No?")

        #print passed response value in terminal
        print(response)

    drop_label = Label(msg_window, text="Select an option from the dropdown:", font="Verdana 10 bold").pack(pady=(25,10))

    #declaring new list to populate dropdown menu (no key:value pairs)
    MODES_dropdown = []

    #loop to populate new dropdown list
    for i in range (0, len(MODES)):
        MODES_dropdown.append(MODES[i][0])

    drop = OptionMenu(msg_window, msg_window_drop, *MODES_dropdown)

    drop.pack(pady=(0,25))
    Button(msg_window, text="Popup From Dropdown Menu", command=lambda: drop_popup(msg_window_drop.get())).pack()


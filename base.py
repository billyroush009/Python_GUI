from tkinter import *
from PIL import ImageTk,Image
import os

#functions from outside python files
from programs.calculator import calculator_launch
from programs.images import image_launch
from programs.message import message_launch
from programs.db import db_launch
from programs.weather import weather_launch

root = Tk()
root.title('Python GUI Examples')
root.iconbitmap('images/sun.ico')

main_label = Label(root, text="Select an example program from the buttons below: ", font=("Verdana 10 bold"))

#root window button declarations
#calculator menu button
calculator_button = Button(root,
    text="Calculator",
    height=3,
    width=30,
    command=calculator_launch)
#image viewer menu button
image_viewer_button = Button(root,
    text="Image Viewer",
    height=3,
    width=30,
    command=image_launch)
#message menu button
message_button = Button(root,
    text="Message Examples",
    height=3,
    width=30,
    command=message_launch)
#db menu button
db_button = Button(root,
    text="Database Example",
    height=3,
    width=30,
    command=db_launch)
weather_button = Button(root,
    text="Weather (API) Example",
    height=3,
    width=30,
    command=weather_launch)

main_label.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
#placing buttons
calculator_button.grid(row=1, column=0, sticky='nesw')
image_viewer_button.grid(row=2, column=0, sticky='nesw')
message_button.grid(row=3, column=0, sticky='nesw')
db_button.grid(row=4, column=0, sticky='nesw')
weather_button.grid(row=5, column=0, sticky='nesw')

mainloop()
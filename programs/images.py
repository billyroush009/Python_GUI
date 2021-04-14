from tkinter import *
from PIL import ImageTk,Image
import os, os.path

def image_launch():
    image_window = Toplevel()
    image_window.title('Image Viewer')
    image_window.iconbitmap('images/sun.ico')
    image_window.geometry("185x175")

    #method to load all .png pictures in the "images" folder into the list instead of statically assigning
    image_list = []
    path = "images"
    #list of valid image types, using .png and jpg for this example
    valid_images = [".png", ".jpg"]
    for image in os.listdir(path):
        #ext used as a check for each file in the directory, splits off the "extension"
        ext = os.path.splitext(image)[1]
        #if file isn't .png from "valid_images" list, skip
        if ext.lower() not in valid_images:
            continue
        #append to list of images, last parenthesis merges "images" with the actual image name (same as comment below)
        #print(path + '\\' + image) #logically the same as final param below
        image_list.append(ImageTk.PhotoImage(Image.open(os.path.join(path,image))))

    #my_label needs to be declared global here otherwise it is undefined w/ these nested functions
    global my_label
    my_label = Label(image_window, image=image_list[0])
    my_label.grid(row=0, column=0, columnspan=3)

    #status message to append to bottom of photo viewer
    status = Label(image_window, text="image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    #functions for scrolling buttons
    def forward(image_number):
        global my_label
        global button_forward
        global button_back

        #grid function to destroy previous image
        my_label.grid_forget()
        #rebuilding the label to display the next image
        my_label = Label(image_window, image=image_list[image_number-1])
        #rebuilding the buttons so they point to the previous/next image
        button_forward = Button(image_window, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(image_window, text="<<", command=lambda: back(image_number-1))
        status = Label(image_window, text="image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

        #catch if there are no more images in the list to load
        if (image_number+1) > len(image_list):
            #passes '1' to forward command so that the button will load index[0] of picture list on next press
            button_forward = Button(image_window, text=">>", command=lambda: forward(1))

        #placing updated elements back on the screen (in same positions)
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0, padx=(10, 0))
        button_forward.grid(row=1, column=2)
        status.grid(row=2, column=0, columnspan=3, sticky='e')
        
    #function to navigate backwards through images
    def back(image_number):
        global my_label
        global button_forward
        global button_back

        #grid function to destroy previous image
        my_label.grid_forget()
        #rebuilding the label to display the next image
        my_label = Label(image_window, image=image_list[image_number-1])
        #rebuilding the buttons so they point to the previous/next image
        button_forward = Button(image_window, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(image_window, text="<<", command=lambda: back(image_number-1))
        status = Label(image_window, text="image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

        #if the next list image would drop index below 0 (before first image)
        if (image_number-1) < 0:
            #button is set to call function w/ last picture in list as 'image_number'
            button_back = Button(image_window, text="<<", command=lambda: back(len(image_list) - 1))
            #status bar set to be x out of x, representing last image in list of images
            status = Label(image_window, text="image " + str(len(image_list)) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

        #placing updated elements back on the screen (in same positions)
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0, padx=(10, 0))
        button_forward.grid(row=1, column=2)
        status.grid(row=2, column=0, columnspan=3, sticky='e')


    #declaring scrolling buttons
    button_back = Button(image_window, text="<<", command=lambda: back(0))
    button_forward = Button(image_window, text=">>", command=lambda: forward(2))
    #button to close out the viewer window
    button_quit = Button(image_window, text="Close Window", command=image_window.destroy)

    #actually placing buttons on the screen
    button_back.grid(row=1, column=0, padx=(10, 0))
    button_quit.grid(row=1, column=1, pady=10, padx=10)
    button_forward.grid(row=1, column=2)
    #sticky stretches elements in cardinal directions
    status.grid(row=2, column=0, columnspan=3, sticky='e')

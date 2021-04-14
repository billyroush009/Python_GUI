# Python_GUI

### Video Demo: https://www.youtube.com/watch?v=5IodgAEru9s

### Setup:
Make sure you have the latest version of Python installed as well as Git. Open Git in the directory you'd like the app saved in. 

```
git clone https://github.com/billyroush009/Python_GUI.git
```

```
pip install -r Python_GUI/requirements.txt
```

```
python Python_GUI/base.py
```

#### Description:
This program uses Python (and tkinter) to run calculator, image viewer, pop-up selector, database (address book), and API (weather conditions) apps from a main menu. 

## base.py:
This file holds the code for the main menu of the application. The menu contains six buttons that all link to python files in the "programs" directory that launch the selected program in a new window.

## calculator.py:
This file holds all the design and logic to make the calculator function. This calculator does simple arithmetic with floats and will display the result with two decimal places. It supports consecutive equals presses and will throw an error if trying to divide by 0.

## images.py:
Contents for the image viewing application. This application reads in all the .png and .jpg files from the "images" folder and then displays them one at a time. A ticker on the bottom shows which number image you are viewing out of the total read in.

## db.py:
This file contains all the design and logic to make the database portion of this app function. It establishes a connection to the "address_book" database if it exists and will otherwise create it with all the proper tables. Hitting the "submit" button will enter the information from the boxes above into the database and the "show records" button will display them at the bottom of the window. By entering in the primary key of an existing record into the "Select ID" entry field, the user can utilize the "Delete Record" and "Edit Record" buttons below.

## message.py:
Contains the design and logic for the pop up samples app. This app lets the user select what type of messagebox will be displayed in either a list of radio buttons or from a drop down menu. A button below either will generate a sample message reflecting what has been chosen.

## weather.py:
File for all the relevant components of the weather API app. This app let's a user enter a ZIP code then calls on three seperate API's to display information about their air quality or other weather conditions below. The color of the screen will change depending on the level of air pollutants. Each time the ZIP code is searched the information will be updated.
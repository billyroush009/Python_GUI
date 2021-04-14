from tkinter import *
from PIL import ImageTk,Image
from os import path
import os
import sqlite3

def db_launch():
    sun_icon_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', 'sun.ico'))
    print(sun_icon_path)

    db_window = Toplevel()
    db_window.title('SQL Databases')
    db_window.iconbitmap(sun_icon_path)

    # Databases
    db_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'database', 'address_book.db'))
    print(db_path)

    # If the database doesn't exist, creates w/ table and fields
    if not path.exists(db_path):
        connection = sqlite3.connect(db_path)
        #create cursor to access db
        cursor = connection.cursor()
        #create db table w/ fields
        cursor.execute("""CREATE TABLE addresses (
                    first_name text,
                    last_name text,
                    address text,
                    city text,
                    state text,
                    zipcode integer)
        """)
        print("DB created w/ Table!")
    else:
        #if db already exists, establish connection and cursor variables
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        print("DB already exists, connection established!")

    #function to del existing record
    def delete_record():
        #re-establishing label that displays rows of db
        global query_label
        query_label.destroy()

        # Create a database or connect to one, must re-establish in function
        connection = sqlite3.connect(db_path)
        #create cursor to access db
        cursor = connection.cursor()

        #deletes from table where oid is the value from the delete_box
        cursor.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

        delete_box.delete(0, END)

        #how to commit changes to db
        connection.commit()

        #repopulating the label showing entries after removing one
        #query the db, 'oid' is a primary key set by default in sqlite3
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()
        #creating empty var to display db entries
        print_records = ''

        #for loop to navigate through addresses table, each 'record' is an entire row with each field
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
        #re-establishing the labels after the deletion has taken place
        query_label = Label(db_window, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2, sticky='nsew')


        #close connection
        connection.close()


    #submission function
    def submit():
        # Create a database or connect to one, must re-establish in function
        connection = sqlite3.connect(db_path)

        #create cursor to access db
        cursor = connection.cursor()

        # Insert user input into table
        cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_code)",
                    {
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'address': address.get(),
                        'city': city.get(),
                        'state': state.get(),
                        'zip_code': zip_code.get()
                    })

        #how to commit changes to db
        connection.commit()

        #close connection
        connection.close()

        #clear text boxes after submission
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zip_code.delete(0, END)

    #Query function, displays records
    def query():
        global query_label

        # Create a database or connect to one, must re-establish in function
        connection = sqlite3.connect(db_path)
        #create cursor to access db
        cursor = connection.cursor()

        #query the db, 'oid' is a primary key set by default in sqlite3
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()
        #print(records)

        #creating empty var to display db entries
        print_records = ''

        #for loop to navigate through addresses table, each 'record' is an entire row with each field
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

        query_label = Label(db_window, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2, sticky='ns')

        #submit changes to db
        connection.commit()
        #close connection
        connection.close()

    #update function for button in edit window
    def update():
        # Create a database or connect to one, must re-establish in function
        connection = sqlite3.connect(db_path)
        #create cursor to access db
        cursor = connection.cursor()

        record_id = delete_box.get()
        #sql statement, uses a python dictionary in the second half to set variables
        cursor.execute("""UPDATE addresses SET 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode

                WHERE oid = :oid""",
                {
                'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city': city_editor.get(),
                'state': state_editor.get(),
                'zipcode': zip_code_editor.get(),
                'oid': record_id
                })



        #submit changes to db
        connection.commit()
        #close connection
        connection.close()
        #close editing window after submitted
        edit_window.destroy()

    #edit function to update record
    def edit_record():
        global edit_window
        edit_window = Tk()
        edit_window.title('Update a Record')
        edit_window.iconbitmap('images/sun.ico')
        edit_window.geometry("400x300")

        # Create a database or connect to one, must re-establish in function
        connection = sqlite3.connect(db_path)
        #create cursor to access db
        cursor = connection.cursor()

        #variable from delete function that specifies user primary key
        record_id = delete_box.get()
        #query the db, 'oid' is a primary key set by default in sqlite3
        cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = cursor.fetchall()
        #print(records)

        #create global vars for textbox names used in update func
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zip_code_editor

        #entry boxes for edit window
        f_name_editor = Entry(edit_window, width=30)
        f_name_editor.grid(row=0, column=1, pady=(10, 0))
        l_name_editor = Entry(edit_window, width=30)
        l_name_editor.grid(row=1, column=1)
        address_editor = Entry(edit_window, width=30)
        address_editor.grid(row=2, column=1)
        city_editor = Entry(edit_window, width=30)
        city_editor.grid(row=3, column=1)
        state_editor = Entry(edit_window, width=30)
        state_editor.grid(row=4, column=1)
        zip_code_editor = Entry(edit_window, width=30)
        zip_code_editor.grid(row=5, column=1)

        #entry box labels
        f_name_label_editor = Label(edit_window, text="First Name").grid(row=0, column=0, pady=(10, 0))
        l_name_label_editor = Label(edit_window, text="Last Name").grid(row=1, column=0)
        address_label_editor = Label(edit_window, text="Street Address").grid(row=2, column=0)
        city_label_editor = Label(edit_window, text="City").grid(row=3, column=0)
        state_label_editor = Label(edit_window, text="State").grid(row=4, column=0)
        zip_label_editor = Label(edit_window, text="ZIP").grid(row=5, column=0)

        #loop through results
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zip_code_editor.insert(0, record[5])

        #create update button
        edit_button = Button(edit_window, text="Save Edited Record", command=update)
        edit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

        #submit changes to db
        connection.commit()
        #close connection
        connection.close()

    #entry boxes for user input, must be declared and then grid separately otherwise db func fails
    f_name = Entry(db_window, width=30)
    f_name.grid(row=0, column=1, pady=(10, 0))

    l_name = Entry(db_window, width=30)
    l_name.grid(row=1, column=1)

    address = Entry(db_window, width=30)
    address.grid(row=2, column=1)

    city = Entry(db_window, width=30)
    city.grid(row=3, column=1)

    state = Entry(db_window, width=30)
    state.grid(row=4, column=1)

    zip_code = Entry(db_window, width=30)
    zip_code.grid(row=5, column=1)

    delete_box = Entry(db_window, width=30)
    delete_box.grid(row=9, column=1)

    #entry box labels
    f_name_label = Label(db_window, text="First Name").grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(db_window, text="Last Name").grid(row=1, column=0)
    address_label = Label(db_window, text="Street Address").grid(row=2, column=0)
    city_label = Label(db_window, text="City").grid(row=3, column=0)
    state_label = Label(db_window, text="State").grid(row=4, column=0)
    zip_label = Label(db_window, text="ZIP").grid(row=5, column=0)
    delete_box_label = Label(db_window, text="Select ID").grid(row=9, column=0)

    #submit button
    submit_button = Button(db_window, text="Submit", command=submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

    #query button
    query_button = Button(db_window, text="Show Records", command=query)
    query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky='ns')

    #delete button
    delete_button = Button(db_window, text="Delete Record", command=delete_record)
    delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10)

    #create update button
    edit_button = Button(db_window, text="Edit Record", command=edit_record)
    edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10)


    #how to commit changes to db
    connection.commit()

    #close connection
    connection.close()
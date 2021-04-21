from tkinter import *
import sqlite3

root = Tk()

# create database

conn = sqlite3.connect('hotel.db')

# create cursor
cursor = conn.cursor()

# create tables
'''#Commented because we can use these executables only once
cursor.execute("""CREATE TABLE addresses (
             first_name text,
             last_name text,
             address text,
             city text,
             state text,
             zipcode text   
             )""")

cursor.execute("""CREATE TABLE rooms(
             room_number integer,
             status text,
             book_start text,
             book_end text
             )""")
'''

# create submit

def submit():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursor
    cursor = conn.cursor()

    # Insert into client table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   })

    # insert into room table
    cursor.execute("INSERT INTO rooms VALUES (:r_number, :status, :book_start, :book_end)",
                   {
                       'r_number': r_number.get(),
                       'status': status.get(),
                       'book_start': book_start.get(),
                       'book_end': book_end.get()
                   })

    # clear the text boxes for clients
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # clear the text boxes for rooms

    r_number.delete(0, END)
    status.delete(0, END)
    book_start.delete(0, END)
    book_end.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create query
def query():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    our_data = cursor.fetchall()

    # loop our information
    line_print = ''
    for i in our_data[0]:
        line_print += str(i) + "\n"

    query_label = Label(root, text=line_print)
    query_label.grid(row=14, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create text boxes for client
f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=2, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=3, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=4, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=5, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1, padx=20)

# create text boxes for rooms
r_number = Entry(root, width=30)
r_number.grid(row=8, column=1, padx=20)

status = Entry(root, width=30)
status.grid(row=9, column=1, padx=20)

book_start = Entry(root, width=30)
book_start.grid(row=10, column=1, padx=20)

book_end = Entry(root, width=30)
book_end.grid(row=11, column=1, padx=20)

# create client section text
room_section = Label(root, text="Client personal data")
room_section.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create text box labels for clients
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=0)

l_name_label = Label(root, text="Second Name")
l_name_label.grid(row=2, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)

city_label = Label(root, text="City")
city_label.grid(row=4, column=0)

state_label = Label(root, text="State")
state_label.grid(row=5, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=6, column=0)

# create room section text
room_section = Label(root, text="Room information")
room_section.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create text box labels for rooms
r_number_label = Label(root, text="Room number")
r_number_label.grid(row=8, column=0)

status_label = Label(root, text="Status")
status_label.grid(row=9, column=0)

book_start_label = Label(root, text="Book start date")
book_start_label.grid(row=10, column=0)

book_end_label = Label(root, text="Book end date")
book_end_label.grid(row=11, column=0)

# create submit button
submit_button = Button(root, text="Save", command=submit)
submit_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button
query_button = Button(root, text="Show book informations", command=query)
query_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=47)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()

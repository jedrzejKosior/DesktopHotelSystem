from tkinter import *
import sqlite3

root = Tk()
root.title("Hotel Management System")
# root.geometry("448x600")

# create database or open

conn = sqlite3.connect('hotel.db')

# create cursor
cursor = conn.cursor()

# create tables
# Commented because we can use these executables only once
cursor.execute("""CREATE TABLE clients (
             first_name text,
             last_name text,
             address text,
             city text,
             state text,
             zipcode text,
             room_number integer   
             )""")

cursor.execute("""CREATE TABLE rooms(
             room_number integer,
             status text,
             book_start text,
             book_end text,
             payment_status text
             )""")

# NIE WIEM CZEMU TA PĘTLA NIE DZIAŁA
# cursor.execute("""FOR iterable IN 1..14 LOOP
#                 INSERT INTO rooms VALUES (iterable, :status, :book_start, :book_end, :payment_status)
#                 END LOOP""",
#                {
#                    'status': 'Clear',
#                    'book_start': 'None',
#                    'book_end': 'None',
#                    'payment_status': 'None'
#                })

cursor.execute("INSERT INTO rooms VALUES (1, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (2, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (3, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (4, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (5, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (6, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (7, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (8, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (9, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (10, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (11, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (12, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (13, 'Clear', 'None', 'None', 'None')")
cursor.execute("INSERT INTO rooms VALUES (14, 'Clear', 'None', 'None', 'None')")


# create submit

def submit():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursor
    cursor = conn.cursor()

    # Insert into client table
    cursor.execute("INSERT INTO clients VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :r_number)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get(),
                       'r_number': r_number.get()
                   })

    # Update into room table
    cursor.execute("""UPDATE rooms SET 
                    status = :status,
                    book_start = :book_start,
                    book_end = :book_end,
                    payment_status = :payment_status
                    WHERE
                    room_number = :r_number""",
                   {
                       'r_number': r_number.get(),
                       'status': status.get(),
                       'book_start': book_start.get(),
                       'book_end': book_end.get(),
                       'payment_status': payment_status.get()
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
    payment_status.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create query
def query_clients():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM clients")
    our_data = cursor.fetchall()

    # loop our information
    line_print = ''
    for i in our_data:
        line_print += str(i[0]) + " " + str(i[1]) + ", " + str(i[2]) + ", " + str(i[3]) + ", " + str(i[4]) + " " + str(
            i[5]) + ", room: " + str(i[6]) + " (id: " + str(i[7]) + ")\n"

    query_label = Label(root, text=line_print)
    query_label.grid(row=15, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


def query_rooms():
    room_table_view = Tk()
    room_table_view.title("Room Information")
    # editor.geometry("448x600")

    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursors
    cursor = conn.cursor()

    # query the database for room information
    cursor.execute("SELECT * FROM rooms")
    our_data = cursor.fetchall()

    # create room section text
    room_section = Label(room_table_view, text="Room information")
    room_section.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

    # create text box labels for rooms
    r_number_for_rooms_label_query = Label(room_table_view, text="Room number")
    r_number_for_rooms_label_query.grid(row=1, column=0, padx=10)

    status_label_query = Label(room_table_view, text="Status")
    status_label_query.grid(row=1, column=1, padx=10)

    book_start_label_query = Label(room_table_view, text="Book start date")
    book_start_label_query.grid(row=1, column=2, padx=10)

    book_end_label_query = Label(room_table_view, text="Book end date")
    book_end_label_query.grid(row=1, column=3, padx=10)

    payment_status_label_query = Label(room_table_view, text="Payment Status")
    payment_status_label_query.grid(row=1, column=4, padx=10)

    for i in range(14):
        for j in range(5):
            if (i != 13):
                loop_query = Label(room_table_view, text=our_data[i][j])
                loop_query.grid(row=2 + i, column=0 + j, padx=10)
            else:
                loop_query = Label(room_table_view, text=our_data[i][j])
                loop_query.grid(row=2 + i, column=0 + j, pady=(0, 10), padx=10)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create delete function
def delete():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursor
    cursor = conn.cursor()

    # delete a record
    cursor.execute("DELETE FROM clients WHERE oid= " + client_id_for_delete.get())

    client_id_for_delete.delete(0, END)
    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create edition save function for clients
def save_edition():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursors
    cursor = conn.cursor()

    record_id = client_or_room_id_for_edit.get()

    cursor.execute("""UPDATE clients SET
                 first_name = :first_name_update,
                 last_name = :last_name_update,
                 address = :address_update,
                 city = :city_update,
                 state = :state_update,
                 zipcode = :zipcode_update,
                 room_number = :room_number_update   
                 
                 WHERE oid = :oid_for_update""",
                   {
                       'first_name_update': f_name_editor.get(),
                       'last_name_update': l_name_editor.get(),
                       'address_update': address_editor.get(),
                       'city_update': city_editor.get(),
                       'state_update': state_editor.get(),
                       'zipcode_update': zipcode_editor.get(),
                       'room_number_update': r_number_editor.get(),
                       'oid_for_update': record_id,
                   })

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create edition save function for rooms
def save_edition_for_rooms():
    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursors
    cursor = conn.cursor()

    record_id = client_or_room_id_for_edit.get()
    cursor.execute("""UPDATE rooms SET
                 room_number = :room_number_update,
                 status = :status_update,
                 book_start = :book_start_update,
                 book_end = :book_end_update,
                 payment_status = :payment_status_update

                 WHERE oid = :oid_for_update""",
                   {
                       'room_number_update': r_number_for_rooms_section_editor.get(),
                       'status_update': status_editor.get(),
                       'book_start_update': book_start_editor.get(),
                       'book_end_update': book_end_editor.get(),
                       'payment_status_update': payment_status_editor.get(),
                       'oid_for_update': record_id,
                   })

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# create edit function to change values of records
def edit():
    editor = Tk()
    editor.title("Records Editor")
    # editor.geometry("448x600")

    # create database or connect to one
    conn = sqlite3.connect('hotel.db')

    # create cursors
    cursor = conn.cursor()
    cursor_for_rooms = conn.cursor()

    # create global variables for our text boxes in editor to access them later in update methods
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global r_number_editor
    global r_number_for_rooms_section_editor
    global status_editor
    global book_start_editor
    global book_end_editor
    global payment_status_editor

    # create text boxes for client
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=4, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=5, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=6, column=1, padx=20)

    r_number_editor = Entry(editor, width=30)
    r_number_editor.grid(row=7, column=1, padx=20)

    # create text boxes for rooms
    r_number_for_rooms_section_editor = Entry(editor, width=30)
    r_number_for_rooms_section_editor.grid(row=10, column=1, padx=20)

    status_editor = Entry(editor, width=30)
    status_editor.grid(row=11, column=1, padx=20)

    book_start_editor = Entry(editor, width=30)
    book_start_editor.grid(row=12, column=1, padx=20)

    book_end_editor = Entry(editor, width=30)
    book_end_editor.grid(row=13, column=1, padx=20)

    payment_status_editor = Entry(editor, width=30)
    payment_status_editor.grid(row=14, column=1, padx=20)

    # create client section text
    room_section_editor = Label(editor, text="Client personal data")
    room_section_editor.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    # create text box labels for clients
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=1, column=0, padx=10)

    l_name_label_editor = Label(editor, text="Second Name")
    l_name_label_editor.grid(row=2, column=0, padx=10)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=3, column=0, padx=10)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=4, column=0, padx=10)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=5, column=0, padx=10)

    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=6, column=0, padx=10)

    r_number_label_editor = Label(editor, text="Room number")
    r_number_label_editor.grid(row=7, column=0, padx=10)

    # create room section text
    room_section_editor = Label(editor, text="Room information")
    room_section_editor.grid(row=9, column=0, columnspan=2, pady=10, padx=10)

    # create text box labels for rooms
    r_number_for_rooms_label_editor = Label(editor, text="Room number")
    r_number_for_rooms_label_editor.grid(row=10, column=0, padx=10)

    status_label_editor = Label(editor, text="Status")
    status_label_editor.grid(row=11, column=0, padx=10)

    book_start_label_editor = Label(editor, text="Book start date")
    book_start_label_editor.grid(row=12, column=0, padx=10)

    book_end_label_editor = Label(editor, text="Book end date")
    book_end_label_editor.grid(row=13, column=0, padx=10)

    payment_status_label_editor = Label(editor, text="Payment Status")
    payment_status_label_editor.grid(row=14, column=0, padx=10)

    # create submit button fro clients
    submit_button_editor = Button(editor, text="Save client changes", command=save_edition)
    submit_button_editor.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=70)

    # create submit button for rooms
    submit_button_editor = Button(editor, text="Save room changes", command=save_edition_for_rooms)
    submit_button_editor.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=70)

    record_id = client_or_room_id_for_edit.get()

    # Query the database
    cursor.execute("SELECT * FROM clients WHERE oid = " + record_id)
    our_data = cursor.fetchall()

    for i in our_data:
        f_name_editor.insert(0, i[0]),
        l_name_editor.insert(0, i[1]),
        address_editor.insert(0, i[2]),
        city_editor.insert(0, i[3]),
        state_editor.insert(0, i[4]),
        zipcode_editor.insert(0, i[5]),
        r_number_editor.insert(0, i[6])

    # query the database for room information
    cursor_for_rooms.execute("SELECT * FROM rooms WHERE oid = " + record_id)
    our_data_for_rooms = cursor_for_rooms.fetchall()

    for i in our_data_for_rooms:
        r_number_for_rooms_section_editor.insert(0, i[0]),
        status_editor.insert(0, i[1]),
        book_start_editor.insert(0, i[2]),
        book_end_editor.insert(0, i[3]),
        payment_status_editor.insert(0, i[4])

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

payment_status = Entry(root, width=30)
payment_status.grid(row=12, column=1, padx=20)

# client id needed for delete
client_id_for_delete = Entry(root, width=30)
client_id_for_delete.grid(row=19, column=0, padx=20)

# client or room id needed to edit
client_or_room_id_for_edit = Entry(root, width=30)
client_or_room_id_for_edit.grid(row=21, column=0, padx=20)

# create client section text
room_section = Label(root, text="Client personal data")
room_section.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

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
room_section.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

# create text box labels for rooms
r_number_label = Label(root, text="Room number")
r_number_label.grid(row=8, column=0)

status_label = Label(root, text="Status")
status_label.grid(row=9, column=0)

book_start_label = Label(root, text="Book start date")
book_start_label.grid(row=10, column=0)

book_end_label = Label(root, text="Book end date")
book_end_label.grid(row=11, column=0)

payment_status_label = Label(root, text="Payment Status")
payment_status_label.grid(row=12, column=0)

# create delete section
room_section = Label(root, text="Delete client with id entered below ")
room_section.grid(row=18, column=0, columnspan=2, pady=10, padx=10)

# create edit section
room_section = Label(root, text="Edit client or room with id entered below")
room_section.grid(row=20, column=0, columnspan=2, pady=10, padx=10)

# create submit button
submit_button = Button(root, text="Save", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button for clients
query_button = Button(root, text="Show client informations", command=query_clients)
query_button.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=47)

# create query button for rooms
query_button_rooms = Button(root, text="Show room informations", command=query_rooms)
query_button_rooms.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=47)

# create delete client button
delete_button = Button(root, text="Delete client", command=delete)
delete_button.grid(row=19, column=1, pady=10, padx=10, ipadx=58)

# create edit button
edit_button = Button(root, text="Edit", command=edit)
edit_button.grid(row=21, column=1, pady=10, padx=10, ipadx=82)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()

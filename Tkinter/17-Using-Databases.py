# ###### Using Databases ######

# =================================
# Importing modules
import sqlite3
import tkinter as tk
from PIL import ImageTk, Image
# =================================
# Configuring our window

root = tk.Tk()
root.title("Using Databases")
root.iconbitmap("icon_name.ico")
root.geometry("400x400")
# =================================
# Creating a database connect object
conn = sqlite3.connect("address_book.db")

# Creating a cursor
cur = conn.cursor()
# =================================
# Creating a table

'''
cur.execute("""
            CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
    """)
'''
# =================================
# ### Creating entry fields ###

f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)
# =================================
# ### Creating entry fields labels ###

f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = tk.Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = tk.Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)
# =================================
# ### Functions for buttons ###

# Submit button functionality


def submit():
    with conn:
        cur.execute("""
            INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode);""",
                    {"f_name": f_name.get(), "l_name": l_name.get(), "address": address.get(), "city": city.get(), "state": state.get(), "zipcode": zipcode.get()})

    # Clear the entry fields
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)


def query():
    with conn:
        cur.execute("SELECT *, oid FROM addresses")
        # oid is the primary key which is automatically set by sqlite3
        records = cur.fetchall()

        # Looping through all records
        showing_records = ""
        for record in records:
            showing_records += f"{record[0]} {record[1]} {record[-1]} \n"

        query_label = tk.Label(root, text=showing_records)
        query_label.grid(row=12, column=0, columnspan=2)


def delete():
    with conn:
        cur.execute(f"DELETE FROM addresses WHERE oid={delete_box.get()}")

    delete_box.delete(0, tk.END)


def update():
    record_id = delete_box.get()

    with conn:
        cur.execute("""UPDATE addresses SET
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode

                    WHERE oid = :oid""",
                    {
                        "first": f_name_editior.get(),
                        "last": l_name_editior.get(),
                        "address": address_editior.get(),
                        "city": city_editior.get(),
                        "state": state_editior.get(),
                        "zipcode": zipcode_editior.get(),
                        "oid": record_id
                    })

        editior.destroy()


def edit():
    global editior

    editior = tk.Tk()
    editior.title("Upadte the record")
    editior.iconbitmap("icon_name.ico")
    editior.geometry("400x400")

    record_id = delete_box.get()

    with conn:
        cur.execute(f"SELECT * FROM addresses WHERE oid={record_id}")

    global f_name_editior
    global l_name_editior
    global address_editior
    global city_editior
    global state_editior
    global zipcode_editior

    # ### Creating entry fields ###

    f_name_editior = tk.Entry(editior, width=30)
    f_name_editior.grid(row=0, column=1, padx=20)

    l_name_editior = tk.Entry(editior, width=30)
    l_name_editior.grid(row=1, column=1, padx=20)

    address_editior = tk.Entry(editior, width=30)
    address_editior.grid(row=2, column=1, padx=20)

    city_editior = tk.Entry(editior, width=30)
    city_editior.grid(row=3, column=1, padx=20)

    state_editior = tk.Entry(editior, width=30)
    state_editior.grid(row=4, column=1, padx=20)

    zipcode_editior = tk.Entry(editior, width=30)
    zipcode_editior.grid(row=5, column=1, padx=20)

    # ### Creating entry fields labels ###

    f_name_editior_label = tk.Label(editior, text="First Name")
    f_name_editior_label.grid(row=0, column=0)

    l_name_editior_label = tk.Label(editior, text="Last Name")
    l_name_editior_label.grid(row=1, column=0)

    address_editior_label = tk.Label(editior, text="Address")
    address_editior_label.grid(row=2, column=0)

    city_editior_label = tk.Label(editior, text="City")
    city_editior_label.grid(row=3, column=0)

    state_editior_label = tk.Label(editior, text="State")
    state_editior_label.grid(row=4, column=0)

    zipcode_editior_label = tk.Label(editior, text="Zipcode")
    zipcode_editior_label.grid(row=5, column=0)

    records = cur.fetchall()
    for record in records:
        f_name_editior.insert(0, record[0])
        l_name_editior.insert(0, record[1])
        address_editior.insert(0, record[2])
        city_editior.insert(0, record[3])
        state_editior.insert(0, record[4])
        zipcode_editior.insert(0, record[5])

    # ### Save button ###
    save_button = tk.Button(editior, text="Save Record", command=update)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)
# =================================
# ### Creating Buttons ###

# Submit button
submit_button = tk.Button(root, text="Add Record To Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Query button
query_button = tk.Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

# Delete button
delete_button = tk.Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

# Create an Update button
edit_button = tk.Button(root, text="Edit Record", command=edit)
edit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=143)
# =================================
root.mainloop()

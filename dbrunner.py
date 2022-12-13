import tkinter as tk
import sqlite3
import os



# create a new database
conn = sqlite3.connect('product.sqlite')
cursor = conn.cursor()




# create the root window
root = tk.Tk()
root.geometry("700x600")

# set the background color of the root window to yellow
root.configure(bg="yellow")


# create a frame
frame = tk.Frame(root, bg="yellow", width=600, height=500)

# centralize the app within the window
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.grid()

# create labels for Id, SerialNumber, Type, and Price
# create labels for Id, SerialNumber, Type, and Price
id_label = tk.Label(frame, text="Id:")
id_label.grid(row=0, column=0)

serial_number_label = tk.Label(frame, text="Serial Number:")
serial_number_label.grid(row=1, column=0)

name_label = tk.Label(frame, text="Name:")
name_label.grid(row=2, column=0)

type_label = tk.Label(frame, text="Type:")
type_label.grid(row=3, column=0)

price_label = tk.Label(frame, text="Price:")
price_label.grid(row=4, column=0)

# create entry fields for Id, SerialNumber, Type, and Price
id_entry = tk.Entry(frame)
id_entry.grid(row=0, column=1)

serial_number_entry = tk.Entry(frame)
serial_number_entry.grid(row=1, column=1)

name_entry = tk.Entry(frame)
name_entry.grid(row=2, column=1)

type_entry = tk.Entry(frame)
type_entry.grid(row=3, column=1)

price_entry = tk.Entry(frame)
price_entry.grid(row=4, column=1)

# import the PhotoImage class from the tkinter.PhotoImage module

# import the Image and PhotoImage classes from the PIL and PIL.ImageTk modules
from PIL import Image
from PIL.ImageTk import PhotoImage

# create a label to display the image
image_label = tk.Label(frame, bg="yellow")

# load the image file and create a PhotoImage object
image = Image.open("arasaka.png").resize((200, 200))
photo_image = PhotoImage(image=image)

# set the image on the label
image_label.configure(image=photo_image)

# position the label on the right side of the app
image_label.place(relx=1, rely=0.5, anchor="e")



def save_product():
    # get the product data from the entry fields
    id = id_entry.get()
    serialnumber = serial_number_entry.get()
    name = name_entry.get()
    type = type_entry.get()
    price = price_entry.get()
    
    # insert the product data into the database
    cursor.execute("INSERT INTO products (id, serialnumber, name, type, price) VALUES (?, ?, ?, ?, ?)", 
                   (id, serialnumber, name, type, price))
    conn.commit()
# create a button
button = tk.Button(frame, text="Save", command=save_product)
button.grid(row=5, column=1, columnspan=2)

id_label.configure(text="Id:", bg="yellow")
serial_number_label.configure(text="Serial Number:", bg="yellow")
name_label.configure(text="Name:", bg="yellow")
type_label.configure(text="Type:", bg="yellow")
price_label.configure(text="Price:", bg="yellow")
button.configure(text="Save", bg="blue")

# change the font and size of the labels, fields, and button
id_label.configure(font=("Arial", 16), width=10)
serial_number_label.configure(font=("Arial", 16), width=10)
name_label.configure(font=("Arial", 16), width=10)
type_label.configure(font=("Arial", 16), width=10)
price_label.configure(font=("Arial", 16), width=10)

id_entry.configure(font=("Arial", 16), width=10)
serial_number_entry.configure(font=("Arial", 16), width=10)
name_entry.configure(font=("Arial", 16), width=10)
type_entry.configure(font=("Arial", 16), width=10)
price_entry.configure(font=("Arial", 16), width=10)

button.configure(font=("Arial", 16), width=10)

# create a list of widgets to apply the settings to
widgets = [id_label, serial_number_label, name_label, type_label, price_label,
           id_entry, serial_number_entry, name_entry, type_entry, price_entry,
           button]

# apply the settings to all the widgets in the list
for widget in widgets:
    widget.configure(font=("Arial", 16), width=10)


for i in range(5):
    frame.grid_columnconfigure(i, minsize=600/5)
    frame.grid_rowconfigure(i, minsize=500/5)


# run the main loop
root.mainloop()




# Import module
from tkinter import *

# Create object
root = Tk()
root.geometry("250x250")

# Dropdown menu options
LOCATIONOPTIONS = [
    "Location1",
    "Location2",
    "Location3",
    "Location4"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Select Location")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *LOCATIONOPTIONS)
drop.pack()

# Execute tkinter
root.mainloop()
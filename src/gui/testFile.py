# Import module
from tkinter import *

# Create object
root = Tk()
root.title("Crime in the UK")
root.geometry("300x250")

# Dropdown menu options
LOCATIONOPTIONS = [
    "London",
    "Wilshire",
    "Manchester",
    "York"
]

CATEGORYOPTIONS = [
    "Burglary",
    "Murder",
    "Rape",
    "Tax evasion"
]

# datatype of menu text
clickedLoc = StringVar()
clickedCat = StringVar()

# initial menu text
clickedLoc.set("Select Location")
clickedCat.set("Select Category")

# Create Dropdown menu
drop1 = OptionMenu(root, clickedLoc, *LOCATIONOPTIONS)
drop2 = OptionMenu(root, clickedCat, *CATEGORYOPTIONS)

drop1.pack()
drop2.pack()

# Execute tkinter
root.mainloop()
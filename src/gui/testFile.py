# Import module
from tkinter import *

# Create object
root = Tk()
root.title("Crime in the UK")
root.geometry("300x250")

class locationDropdown:

    LOCATIONOPTIONS = [
        "London",
        "Wilshire",
        "Manchester",
        "York"
    ]

    clickedLoc = StringVar()
    clickedLoc.set("Select Location")
    drop1 = OptionMenu(root, clickedLoc, *LOCATIONOPTIONS)
    drop1.pack()

class categoryDropdown:

    CATEGORYOPTIONS = [
        "Burglary",
        "Murder",
        "Rape",
        "Tax evasion"
    ]

    clickedCat = StringVar()
    clickedCat.set("Select Category")
    drop2 = OptionMenu(root, clickedCat, *CATEGORYOPTIONS)
    drop2.pack()

# Execute tkinter
root.mainloop()
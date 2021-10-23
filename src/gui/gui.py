from tkinter import *

# Initializes Tkinter
root = Tk()

# Creating a Label Widget
welcomeLabel = Label(root, text="Welcome to CriminalityUK")
instructionLabel = Label(root, text="Press the buttons")

# Shoving it onto the screen
welcomeLabel.grid(row=0, column=0)
instructionLabel.grid(row=1, column=0)

# Keeps window running
root.mainloop()

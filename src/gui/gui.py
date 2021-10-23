from tkinter import *

# Initializes Tkinter
root = Tk()


# Functions
def click_category_button():

    response_string = "Entered Category: " + entryCategory.get()
    category_label = Label(root, text=response_string)
    category_label.grid(row=2, column=0)


# Creating Widgets
welcomeLabel = Label(root, text="Welcome to CriminalityUK")
instructionLabel = Label(root, text="Press the buttons")
entryCategory = Entry(root)  # Will be dropdown later
entryCategory.insert(0, "Enter Category:")
categoryButton = Button(root, command=click_category_button, text="Show Category", padx=50, pady=5)

# Shoving it onto the screen
welcomeLabel.grid(row=0, column=0)
instructionLabel.grid(row=1, column=0)
entryCategory.grid(row=1, column=1)
categoryButton.grid(row=2, column=1)

# Keeps window running
root.mainloop()

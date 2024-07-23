# here i am creating a GUI based python program using tkinter for converting any text into its hash value

from tkinter import *  # importing all the functions and classes and everthing from tkinter
import hashlib  # importing the hashlib library

# creating the main window
admin = Tk()
admin.title("Text to Hash Value convertor")
admin.geometry("700x300")

# creating a function for hash conversion
def calc_hash():
    text = entry.get()
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    result_label.config(text="Hashed value: " + hashed_text)


# creating a label for the input entry
input_label=Label(admin, text="Enter the text: ")
input_label.pack()

entry = Entry(admin)
entry.pack()

# creating a button for calculation of the hash value
calc_button = Button(admin, text="Calculate Hash", command = calc_hash)
calc_button.pack()

# creating a label for the display of the hash value
result_label = Label(admin)
result_label.pack()

# run the application
admin.mainloop()
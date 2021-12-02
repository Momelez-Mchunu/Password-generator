from tkinter import *
from random import randint


root = Tk()
root.title('Password generator')
root.geometry('500x300')

labelFrame =  LabelFrame(root, text="How many characters?")
labelFrame.pack(pady=20)

entry = Entry(labelFrame,font=("Helvetica",24))
entry.pack(pady=20,padx=20)

password_entry = Entry(root, text="",font=("Helvetica",24))
password_entry.pack(pady=20)

my_frame = Frame(root)

my_frame.pack(pady=20)

generate_button = Button(my_frame,text="Generate password")
generate_button.grid(row=0,column=0,padx=10)

clip_button =  Button(my_frame,text="Copy to clipboard")
clip_button.grid(row=0,column=1,padx=10)
root.mainloop()
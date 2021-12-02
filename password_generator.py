from tkinter import Entry,LabelFrame,Frame,Button,Tk
from random import choice as choice
from tkinter.constants import END

def gen_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()~`-_.,?1234567890'
    password_entry.delete(0,END)
    pass_length = int(entry.get())
    password=""
    for x in range(pass_length):
        password +=choice(chars)
    password_entry.insert(0,password)
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

generate_button = Button(my_frame,text="Generate password",command=gen_password)
generate_button.grid(row=0,column=0,padx=10)

clip_button =  Button(my_frame,text="Copy to clipboard")
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()
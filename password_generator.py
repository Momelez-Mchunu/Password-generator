from tkinter import Entry,LabelFrame,Frame,Button,Tk
from random import choice as choice
from tkinter.constants import END

def gen_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()~`-_.,?1234567890'

    #Clear recently generated password
    password_entry.delete(0,END)
    pass_length = int(entry.get())
    password=""

    # generate password and display it
    for x in range(pass_length):
        password +=choice(chars)
    password_entry.insert(0,password)
def clipboard():
    pass
root = Tk()
root.title('Password generator')
root.geometry('500x300')

labelFrame =  LabelFrame(root, text="How many characters?")
labelFrame.pack(pady=20)

entry = Entry(labelFrame,font=("Helvetica",24))
entry.pack(pady=20,padx=20)

password_entry = Entry(root, text="",font=("Helvetica",24),bg="systembuttonface",bd=0)
password_entry.pack(pady=20)

my_frame = Frame(root)

my_frame.pack(pady=20)

generate_button = Button(my_frame,text="Generate password",command=gen_password)
generate_button.grid(row=0,column=0,padx=10)

clip_button =  Button(my_frame,text="Copy to clipboard")
clip_button.grid(row=0,column=2,padx=10)

close_button = Button(my_frame,text="Close",command=root.destroy)
close_button.grid(row=1,column=1,padx=10)

root.mainloop()
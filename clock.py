from tkinter import * #standard python GUI library #thin object-oriented layer on top of Tcl/Tk
from tkinter.ttk import * #seprate ,to extent possible #to style tkinter widgets 


from time import strftime #retrieves the time  #strftime:func to change date and time objects to strings
root = Tk()
root.title("Clock")
def time():
    string =strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label = Label(root, font =("ds-digital", 80),background = "olive", foreground="black")
label.pack(anchor='center')
time()
mainloop()


from tkinter import *

w = Tk()

photo = PhotoImage(file='car.gif')
label = Label(w, image=photo)
label.pack()

w.mainloop()

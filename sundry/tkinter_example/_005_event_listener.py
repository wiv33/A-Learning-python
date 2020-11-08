from tkinter import *
from tkinter import messagebox

w = Tk()


def click_left(event):
    messagebox.showinfo("", "click !!")


w.bind('<Button>', click_left)

w.mainloop()

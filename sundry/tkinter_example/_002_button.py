from tkinter import *

w = Tk()

btn = Button(w, text='close', fg='red', command=quit)

btn.pack()

[Button(w, text=f'버튼 {i}').pack(side='right') for i in range(3, 0, -1)]

w.mainloop()

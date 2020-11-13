from tkinter import *

window = Tk()

label1 = Label(window, text='COOK BOOK')
label2 = Label(window, text='열심히', font=('궁서체', 30), fg='blue')
label3 = Label(window, text='공부 중입니다.',
               bg='magenta',
               width=20,
               height=5,
               # anchor - label의 위치를 나타냄
               # 동서남북 기준으로, South East
               anchor=SE)

label1.pack()
label2.pack()
label3.pack()

if __name__ == '__main__':
    window.mainloop()



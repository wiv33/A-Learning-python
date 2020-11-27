from tkinter import *
from tkinter import messagebox
import sqlite3
import os

w = Tk()

root = 'c:\\Temp\\db\\'

if not os.path.exists(root):
    os.makedirs(root)


conn = sqlite3.connect('%suserTable' % root)
cs = conn.cursor()

# cs.executemany('INSERT INTO userTable VALUES (?, ?, ?, ?)',
#                [('1001', 'alpha', 'one', 'one@gamil.com', 1904),
#                 ('2001', 'before', 'noddle', 'noddle@naver.com', 1800),
#                 ('2002', 'vision', 'smart', 'smart@naver.com', 1919),
#                 ('1002', 'asdf', 'ewq', 'ewq@daum.net', 1950),
#                 ('1003', 'joo', 'aass', 'aass@naver.com', 1948)])


# result = cs.execute('CREATE TABLE userTable (id char(4), userName char(15), email char(15), birthYear int)')

def click_left(event):
    cs.execute(f'INSERT INTO userTable VALUES ({os.getpid()}, "John Bann", "john@naver.com", 1990)')
    conn.commit()

    res = cs.execute('SELECT * FROM userTable')
    fetchall = res.fetchall()
    print(fetchall)
    messagebox.showinfo("", fetchall)


w.bind('<Button>', click_left)

w.mainloop()

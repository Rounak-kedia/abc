from tkinter import *
from tkinter import ttk 
root=Tk()

root.title("Spent")
root.geometry('500x500')
root.iconbitmap(r'spent.ico')
'''
bg_pic=PhotoImage(file='l_bgr.jpg')
bgr_label = Label(root, image=bg_pic)
bgr_label.place(x=0, y=0, relwidth=1, relheight=1)
'''
wel_l=Label(root,text = "Welcome to Spent Expense Tracker!")
desc_l=Label(root,text = "Personal Finance made Eassy.")
'''
wel_l.config(font=("Courier", 14))
desc_l.config(font=("Courier", 8))
'''
wel_l.place(relx=0.28,rely=0.3)
desc_l.place(relx=0.301,rely=0.335)

root.mainloop()
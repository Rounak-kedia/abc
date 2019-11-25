from tkinter import *
from tkinter import ttk
def event():
	if v.get()==str(1):
		nl.config(text="expense")
	else:
		nl.config(text="income")

tran_win = Tk()
tran_win.title("Dashboard")
v = StringVar()
v.set(None)
Label(tran_win,text="Add your transaction : ").grid(row=0,column=0,sticky = W, pady = 2)
nl=Label(tran_win,text="Name of Income/expense : ")
nl.grid(row=3,column=0,sticky = W, pady = 2)
Radiobutton(tran_win,text="Expense",variable=v,value =1,command=event).grid(row=2,column=0,sticky = W, pady = 2)
Radiobutton(tran_win,text="Income",variable=v,value =2,command=event).grid(row=2,column=5,sticky = W, pady = 2) 
name=Entry(tran_win).grid(row=3,column=5,sticky = W, pady = 2)
Label(tran_win,text="Amount : ").grid(row=4,column=0,sticky = W, pady = 2)
amt=Entry(tran_win).grid(row=4,column=5,sticky = W, pady = 2)
#take date time from system
Label(tran_win,text="Tags : ").grid(row=5,column=0,sticky = W, pady = 2)
tags=Entry(tran_win).grid(row=5,column=5,sticky = W, pady = 2)
####
#take tags input split and send
####
add=ttk.Button(tran_win, text="Add", width=10)
add.grid(row=6,column=3,sticky = W, pady = 2)


'''
add=Button(dashboard, text="Add a transaction", width=20,activebackground='green',activeforeground='black',anchor=N).pack()
'''
tran_win.mainloop()
import matplotlib, numpy, sys
import sqlite3
from datetime import date
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk

global Ecat,Icat
Ecat=["Entertainment","Utilities","Education","Others"]
Icat=["Salary","Bonus","Gift Income","Pension"]
'''
def daily_summary():
	daily_sum=Frame(dashboard,width=100,height=100)
	##############data retrival
	today = str(date.today()).replace("-","/")
	dte=int(today[-2:])
	if(date<7)
	{
	#################################	if()
	}
	dt=[]
	for i in range(7):
		d=today[0:8]+str(dte-i)
		dt.append(d)
	cursor = conn.execute("SELECT * FROM tracks")
	rows = cursor.fetchall()
	for row in rows:
	    print row
	##############
	Label(daily_sum,text="Here is your daily summary!",anchor=W,justify=LEFT).pack()
	#################################################################################################<graph>
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	data = (20,35,30,35,27,12,5)
	ind = numpy.arange(7)  # the x locations for the groups
	width = .5
	for i in range(7):
		a=dt[i][5:].split("/")
		a.reverse()
		dt[i]="/".join(a)
	dt.reverse()
	rects1 = ax.bar(ind, data, width,tick_label = dt,color = ['red', 'green','blue','black'])
	ax.set_xlabel('Date') 
	ax.set_ylabel('Expense') 
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=daily_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	##################################################################################################
	daily_sum.grid(row=0,column=0)
'''
def budget_summary():
	bud_sum=Frame(dashboard)
	Label(bud_sum,text="Here is your budget summary!").pack()
	#<data retrival>

	cursor=conn.excute("SELECT amount,tag from Expense where eDate Between '%s'"%())
		
	#
	#<graph>
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	labels = ["Food", "Cab", "Medical", "Education"]
	values = [1,2,3,2]
	rects1 = ax.pie(values,labels=labels)
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=bud_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	#
	bud_sum.grid(row=1,column=0)
'''
def earning_summary():
	ear_sum=Frame(dashboard)
	Label(ear_sum,text="Here is your earning summary!").pack()
	##################################################################################################
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	data = [[1,2,3,4,5,6,7],[1,3,24,5,43,2,7]]
	ind = numpy.arange(7)  # the x locations for the groups
	width = .25
	tick_label = ['mon', 'tues', 'wed', 'thur', 'fri','sat','sun']
	rects1 = ax.bar(ind, data[0], width,tick_label = tick_label,color = ['red'])
	rects1 = ax.bar(ind+width, data[1], width,tick_label = tick_label,color = ['green'])
	ax.set_xlabel('Day') 
	ax.set_ylabel('Expense') 
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=ear_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	##################################################################################################
	ear_sum.grid(row=2,column=0)
def add_to_database():
	##get data from global variable

	# add to database

	#show successfull add
	Label(tran_win,text="Transaction Added", fg="green", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)
	#add some timer to remove this or close TLW

def transaction():
	global tran_win
	tran_win = Toplevel(dashboard)
	tran_win.title("Add a trannsaction")
	tran_win.geometry("400x200")
	v = StringVar()
	v.set(1)
	def event():
		if v.get()=="1":
			nl.config(text="Name of Expense : ")
			radio1.config(text="Entertainment")
			radio2.config(text="Utilities")
			radio3.config(text="Education")
			radio4.config(text="Others")
			radioVar.set(0)
		else:
			nl.config(text="Name of Income : ")
			radio1.config(text="Salary")
			radio2.config(text="Bonus")
			radio3.config(text="Gift Income")
			radio4.config(text="Pension")
			radioVar.set(0)
	Label(tran_win,text="Add your transaction : ").grid(row=0,column=0,sticky = W, pady = 2)
	nl=Label(tran_win,text="Name of Expense : ")
	nl.grid(row=3,column=0,sticky = W, pady = 2)
	Radiobutton(tran_win,text="Expense",variable=v,value =1,command=event).grid(row=2,column=0,sticky = W, pady = 2)
	Radiobutton(tran_win,text="Income",variable=v,value =2,command=event).grid(row=2,column=3,sticky = W, pady = 2) 
	name=Entry(tran_win).grid(row=3,column=3,sticky = W, pady = 2)
	Label(tran_win,text="Amount : ").grid(row=4,column=0,sticky = W, pady = 2)
	amt=Entry(tran_win).grid(row=4,column=3,sticky = W, pady = 2)
	#take date time from system
	Label(tran_win,text="Tags : ").grid(row=5,column=0,sticky = W, pady = 2)
	radioVar = BooleanVar()
	radioVar.set(0)
	radio1 = Radiobutton(tran_win,text = "Entertainment", variable = radioVar)
	radio1.grid(row = 5, column = 3, sticky = W,padx=2,pady=2)
	radio2 = Radiobutton(tran_win,text = "Utilities", variable = radioVar)
	radio2.grid(row = 5, column = 5, sticky = W,padx=2,pady=2)
	radio3 = Radiobutton(tran_win,text = "Education", variable =radioVar)
	radio3.grid(row = 6, column = 3, sticky = W,padx=2,pady=2)
	radio4 = Radiobutton(tran_win,text = "Others", variable = radioVar)
	radio4.grid(row = 6, column = 5, sticky = W,padx=2,pady=2)
	add=ttk.Button(tran_win, text="Add", width=10, command=add_to_database)
	add.grid(row=7,column=3,sticky = W, pady = 2)

def add_transaction():
	add_tran=Frame(dashboard)
	add=Button(add_tran, text="Add a transaction", width=20, command = transaction,activebackground='green',activeforeground='black',anchor=N).pack()
	add_tran.grid(row=4,column=0)
'''
##Starter Code
def dashboard_screen():
    global dashboard
    dashboard = Tk()
    dashboard.title("Dashboard")
    #conn = sqlite3.connect('ExpenseTracker.db')
    daily_summary()
    Label(dashboard,text="    ")
    budget_summary()
    earning_summary()
    add_transaction()
    dashboard.mainloop()
dashboard_screen()
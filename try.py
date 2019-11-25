import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sqlite3
from datetime import date
import datetime
from tkinter import *
from tkinter import ttk

global Ecat,Icat,wday
Ecat=["Entertainment","Utilities","Education","Others"]
Icat=["Salary","Bonus","Gift Income","Pension"]
wk={Monday:mon,}

def budget_summary():
	bud_sum=Frame(dashboard)
	Label(bud_sum,text="Here is your budget summary!").pack()
	#<data retrival>

	cursor=conn.excute("SELECT amount,tag from Expense where eDate Between '%s' and '%s'"%(d1,d2))
		
	#
	#<graph>
	f = Figure(figsize=(4,4), dpi=100)
	ax = f.add_subplot(111)
	rects1 = ax.pie(values,labels=Ecat)
	ax.set_title('Daily Expense')
	canvas = FigureCanvasTkAgg(f, master=bud_sum)
	canvas.draw()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
	#
	bud_sum.grid(row=1,column=0)

global dashboard
dashboard = Tk()
dashboard.title("Dashboard")
#
today=str(date.today()).replace("-","/")	#today's date in string format	output : 'dd/mm/yyyy'
tdate=int(today[-2:])	#today's date like 08
day=datetime.datetime.strptime(date, '%d %m %Y').weekday()	#day of week
startdate='01'+today[2:]
#
conn=sqlite3.connect("ExpenseTracker.db")
budget_summary()
dashboard.mainloop()
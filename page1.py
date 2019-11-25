from tkinter import *
from tkinter import ttk
    

root = Tk()   # create a GUI window 
root.geometry("300x250") # set the configuration of GUI window 
root.title("Account Login") # set the title of GUI window

# create a Form label 
ttk.Label(root,text="Choose Login Or Register", width="300", font=("Calibri", 13)).pack() 
ttk.Label(root,text="").pack() 

# create Login Button 
ttk.Button(root,text="Login", width="30").pack() 
ttk.Label(root,text="").pack() 

# create a register button
ttk.Button(root,text="Register", width="30").pack()
 

root.mainloop() # start the GUI

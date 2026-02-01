from tkinter import messagebox 
import tkinter as tk
a = tk.Tk()
a.title("Virus scan")
a.geometry("500x500")

def msg() : 
    messagebox.showwarning("We found a virus.")

button = tk.Button(a, text="Scan computer.", command=msg)
button.place(x=0,y=0)
a.mainloop()
"""Create a Tkinter Application which consists of a root window with a button (with text Scan for the virus). When this button is clicked, it will generate a message box that shows a warning that  Stop! Virus Found."""
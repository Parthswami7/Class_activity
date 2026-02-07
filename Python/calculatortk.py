from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk

root = Tk()
root.geometry('550x550')
root.title('Calculator')
root.configure(bg='white') 

upload = Image.open(r"C:\Users\LENOVO\Desktop\classactivity\Python\q1.jpg")
upload = upload.resize((400,400))
image = ImageTk.PhotoImage(upload)
label = Label(root, bg="Black", image = image ) 
label.place(x=0,y=0) 
label1 = Label(root , bg="black", text="This is fun calculator.")
label1.place(x=10,y=10) 
def msg():
    MsgBox = messagebox.showinfo("alert", "It does not run.")
    if MsgBox == "ok": 
        topwin()

button = Button(root, bg="Blue", fg="White", command=msg)
button.place(x= 500, y=500)
def topwin():
    top = Toplevel(root)
    top.title("Calculator")
    top.configure(bg="Black")
    top.geometry("300x300")

    button.place(x=250, y=250)
    label.place(x=275, y=275)
    label1.place(x=280, y=280)
    top.mainloop()

root.mainloop()
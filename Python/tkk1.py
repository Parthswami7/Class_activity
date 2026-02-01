from PIL import Image, ImageTk 
import tkinter as tk
a = tk.Tk()
a.title("turtle")
a.geometry("500x500")

b = Image.open("1.jpg")
c = ImageTk.PhotoImage(b) 

label = tk.Label(a, image=c , width=400 , height=300)
label.image = c
label.place(x=0, y=0)
label2 = tk.Label(a, text="This is how you add Image as a label")
label2.place(x=1,y=1)
a.mainloop()
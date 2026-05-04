from tkinter import * 
window = Tk()
window.title('tinkter sample window')
window.geometry('500x500')

greeting = Label(text="Hello dear", fg="white", bg="black")
button = Button(text="Click me", fg="white", bg="black")
entry = Entry(bg="blue", fg="White", width="30")

greeting.pack()
button.pack()
entry.pack()
frame = Frame(master="window", relief="RAISED", boderwidth=5)
frame.pack()
label = Label(master=frame, text="Sample frame")
label.pack()
textbox = Text(fg="Black", bg="white")
textbox.pack()

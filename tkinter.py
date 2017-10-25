from Tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button1",fg="blue")
button2 = Button(topFrame, text="Button2",fg="orange")
button3 = Button(topFrame, text="Button3",fg="red")
button4 = Button(bottomFrame, text="Button1",fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()


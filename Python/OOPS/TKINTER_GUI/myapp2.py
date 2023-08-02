from tkinter import *


screen = Tk()

screen.geometry("500x500")
screen.title("My Profile")

btn = Button(screen,text="Click Here",font=("Arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white")
btn.pack(side=LEFT)

btn = Button(screen,text="Click Here",font=("Arial",12,"bold"))
btn.pack(side=TOP)

screen.mainloop()
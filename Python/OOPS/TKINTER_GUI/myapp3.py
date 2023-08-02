from tkinter import *
from random import *

screen = Tk()
screen.geometry("500x500")
screen.title("My Python")

user_var = StringVar()
computer_var = StringVar()

"""
Python Logic Here......

"""

def myLogic(userchoice):
    l1 = ["Rock", "Paper", "Scissor" ]
    print("userchoice === ", userchoice)
    computer_choice = choice(l1)
    print("Computer Choice === ", computer_choice)
    user_var.set(userchoice)
    
btn = Button(screen,text="Rock",font=("Arial",12,"bold"), bg="black", fg="white",activebackground="red",activeforeground="white",command=lambda : myLogic("Rock"))  


btn.place(x=10, y=10)

btn = Button(screen,text="Paper", font=("Arial",12,"bold"),command=lambda : myLogic("Paper"))
btn.place(x=90, y=10)

btn = Button(screen,text="Scissor",font=("Arial",12,"bold"), bg="black",fg="white",activebackground="red",activeforeground="white",command=lambda : myLogic("scissor"))
btn.place(x=170, y=10)


userchoice_display = Label(screen,textvariable=user_var,font=("Arial",12,"bold"),fg="blue")
userchoice_display.place(x=250, y=50)

userchoice_display = Label(screen,textvariable=user_var,font=("Arial",12,"bold"),fg="blue")
userchoice_display.place(x=250, y=50)

computer_display = Label(screen,textvariable=computer_var,font=("Arial",12,"bold"),fg="blue")
userchoice_display.place(x=10, y=100)

computer_display = Label(screen,textvariable=computer_var,font=("Arial",12,"bold"),fg="blue")
userchoice_display.place(x=250, y=100)
screen.mainloop()
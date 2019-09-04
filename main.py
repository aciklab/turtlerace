from tkinter import *
import turtleClass

def myFonsiyon():
    myinput = userinput.get()
    turtleClass.main(myinput)
    mainPage.destroy()

mainPage = Tk()
mainPage.title("Turtle Race")

userinput = Entry(mainPage)
userinput.pack()


click = Button(mainPage,text="Bas",command=myFonsiyon)
click.pack(side='bottom')

mainPage.mainloop()
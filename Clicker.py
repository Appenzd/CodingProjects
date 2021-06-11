from tkinter import *
import time

#defining window
Clicker = Tk()
Clicker.title("Clicker")
Clicker.geometry("500x500")

#variables
Points = IntVar()
Points.set(0)

Increase = IntVar()
Increase.set(1)

Count = IntVar()
Count.set(0)

AutoAdd = IntVar()
AutoAdd.set(0)

GameStatus = StringVar()
GameStatus.set("Game over!")


#clock function to run autoclickers
def clock():
    if AutoAdd.get() >= 1:
        Points.set(Points.get() + AutoAdd.get())
    Clicker.after(1000,clock)

#functions for increase buttons
def IncreaseFunc1():
    if Points.get() >= 50:
        Count.set(Count.get() + 1)
        Increase.set(0)
        Increase.set(Increase.get() + Count.get() * 10)
        Points.set(Points.get() - 50)

def IncreaseFunc2():
    if Points.get() >= 100:
        Count.set(Count.get() + 1)
        Increase.set(0)
        Increase.set(Increase.get() + Count.get() * 50)
        Points.set(Points.get() - 100)

def IncreaseFunc3():
    if Points.get() >= 250:
        Count.set(Count.get() + 1)
        Increase.set(0)
        Increase.set(Increase.get() + Count.get() * 100)
        Points.set(Points.get() - 250)

def IncreaseFunc4():
    if Points.get() >= 500:
        Count.set(Count.get() + 1)
        Increase.set(0)
        Increase.set(Increase.get() + Count.get() * 250)
        Points.set(Points.get() - 500)       

def IncreaseFunc5():
    if Points.get() >= 1000:
        Count.set(Count.get() + 1)
        Increase.set(0)
        Increase.set(Increase.get() + Count.get() * 500)
        Points.set(Points.get() - 1000)        

def AddPoints():
    Points.set(Points.get() + Increase.get())

#functions for auto clickers
def Auto1():
    if Points.get() >= 50:
        AutoAdd.set(AutoAdd.get() + 1)
        Points.set(Points.get() - 50)

def Auto2():
    if Points.get() >= 100:
        AutoAdd.set(AutoAdd.get() + 5)
        Points.set(Points.get() - 100)

def Auto3():
    if Points.get() >= 200:
        AutoAdd.set(AutoAdd.get() + 20)
        Points.set(Points.get() - 200)

def Auto4():
    if Points.get() >= 500:
        AutoAdd.set(AutoAdd.get() + 50)
        Points.set(Points.get() - 5000)

def Auto5():
    if Points.get() >= 1000:
        AutoAdd.set(AutoAdd.get() + 100)
        Points.set(Points.get() - 1000)
    
            
#label to show points
PointsLabel = Label(Clicker, textvariable=Points)
PointsLabel.grid(row=1, column=2)
#label to show game over
GameOver = Label(Clicker, textvariable=Points)
GameOver.grid(row=1, column=1)

#main button to get points
MainButton = Button(Clicker, text="Click Me!", activeforeground="red", command=AddPoints)
MainButton.grid(row=1, column=1)

#clicker buttons
Upgrade1 = Button(Clicker, text="+10 per click(50)", activeforeground="red", command=IncreaseFunc1)
Upgrade1.grid(row=2, column=1)

Upgrade2 = Button(Clicker, text="+50 per click(100)", activeforeground="red", command=IncreaseFunc2)
Upgrade2.grid(row=3, column=1)

Upgrade3 = Button(Clicker, text="+100 per click(250)", activeforeground="red", command=IncreaseFunc3)
Upgrade3.grid(row=4, column=1)

Upgrade4 = Button(Clicker, text="+250 per click(500)", activeforeground="red", command=IncreaseFunc4)
Upgrade4.grid(row=5, column=1)

Upgrade5 = Button(Clicker, text="+500 per click(1000)", activeforeground="red", command=IncreaseFunc5)
Upgrade5.grid(row=6, column=1)

#auto clickers
Auto1 = Button(Clicker, text="+1 every second(50)", activeforeground="red", command=Auto1)
Auto1.grid(row=2, column=2)

Auto2 = Button(Clicker, text="+5 every second(100)", activeforeground="red", command=Auto2)
Auto2.grid(row=3, column=2)

Auto3 = Button(Clicker, text="+20 every second(200)", activeforeground="red", command=Auto3)
Auto3.grid(row=4, column=2)

Auto4 = Button(Clicker, text="+50 every second(500)", activeforeground="red", command=Auto4)
Auto4.grid(row=5, column=2)

Auto5 = Button(Clicker, text="+100 every second(1000)", activeforeground="red", command=Auto5)
Auto5.grid(row=6, column=2)

clock()
Clicker.update()
Clicker.mainloop()
from tkinter import *


def piccolo():
    try:
        global var2
        answer = str(eval(var2))
        var1.set(answer)
    except ZeroDivisionError:
        var1.set("Go back to kindergarten that dosent work") 
    except:
        var1.set("Houston we have a problem")   

def oboe(number):
    global var2
    var2 = var2 + str(number)
    var1.set(var2)
      

def bass():
    global var2
    var2 = ""
    var1.set(var2)

Something = Tk()
Something.title("Calculator")
Something.geometry("500x500")

var1 = StringVar()
var2 = ""


menu = Menu(Something)
r = Menu(menu)
menu.add_cascade(label="File2", menu = r)
r.add_command(label="Exit", command=Something.quit)
Something.config(menu = menu)

a = Button(Something, text="1", fg = "red", height=2, width=10, command=lambda: oboe("1"))
a.grid(row=2, column=0)
b = Button(Something, text="2", fg = "red", height=2, width=10, command=lambda: oboe("2"))
b.grid(row=2, column=1)
c = Button(Something, text="3", fg = "red", height=2, width=10, command=lambda: oboe("3"))
c.grid(row=2, column=2)
d = Button(Something, text="4", fg = "red", height=2, width=10, command=lambda: oboe("4"))
d.grid(row=3, column=0)
e = Button(Something, text="5", fg = "red", height=2, width=10, command=lambda: oboe("5"))
e.grid(row=3, column=1)
f = Button(Something, text="6", fg = "red", height=2, width=10, command=lambda: oboe("6"))
f.grid(row=3, column=2)
g = Button(Something, text="7", fg = "red", height=2, width=10, command=lambda: oboe("7"))
g.grid(row=4, column=0)
h = Button(Something, text="8", fg = "red", height=2, width=10, command=lambda: oboe("8"))
h.grid(row=4, column=1)
i = Button(Something, text="9", fg = "red", height=2, width=10, command=lambda: oboe("9"))
i.grid(row=4, column=2)
j = Button(Something, text="0", fg = "red", height=2, width=10, command=lambda: oboe("0"))
j.grid(row=5, column=1)

k = Button(Something, text="+", fg = "red", height=2, width=10, command=lambda: oboe("+"))
k.grid(row=2, column=3)
l = Button(Something, text="-", fg = "red", height=2, width=10, command=lambda: oboe("-"))
l.grid(row=3, column=3)
m = Button(Something, text="x", fg = "red", height=2, width=10, command=lambda: oboe("*"))
m.grid(row=4, column=3)
n = Button(Something, text="/", fg = "red", height=2, width=10, command=lambda: oboe("/"))
n.grid(row=5, column=3)
o = Button(Something, text="=", fg = "red", height=2, width=10, command=piccolo)
o.grid(row=6, column=3)
p = Button(Something, text=".", fg = "red", height=2, width=10, command=lambda: oboe("."))
p.grid(row=7, column=3)
q = Button(Something, text="Clear", fg = "red", height=2, width=10, command=bass)
q.grid(row=8, column=3)

z = Entry(Something, textvariable=var1)
z.grid(row=1, columnspan=3)


Something.mainloop()

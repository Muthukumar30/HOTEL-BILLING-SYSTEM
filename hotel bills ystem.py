from tkinter import *
window=Tk()
window.geometry("700x500")
window.title("home food hotel")
def calculate():
    rice=e1.get()
    tea=e2.get()
    total=(int(rice)*40)+(int(tea)*10)
    l22= Label(window, text=total, font="times 30 bold")
    l22.place(x=100, y=360)
#-----
l11=Label(window,text="MAIN INDEX",font="times 30 bold")
l11.place(x=350,y=20,anchor="center")

l1=Label(window,text="MENU",font="times 28 bold")
l1.place(x=500,y=100)

l2=Label(window,text="RICE      RS:40",font="times 18 bold")
l2.place(x=450,y=150)

l3=Label(window,text="TEA       RS:10",font="times 18 bold")
l3.place(x=450,y=180)

l4=Label(window,text="FRIED RICE RS:50",font="times 18 bold")
l4.place(x=450,y=210)
#----
l5=Label(window,text="select the item",font="times 18 bold")
l5.place(x=70,y=70)

l6=Label(window,text="rice",font="times 18 bold")
l6.place(x=20,y=120)

l7=Label(window,text="tea",font="times 18 bold")
l7.place(x=250,y=120)
#---------------------
e1=Entry(window)
e1.place(x=20,y=150)

e2=Entry(window)
e2.place(x=250,y=150)
#---------------------
b1=Button(window,text="bill",width=20,command=calculate)
b1.place(x=100,y=300)

window.mainloop()
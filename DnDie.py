from tkinter import Tk
from tkinter import Canvas
from tkinter import Frame
from tkinter import Grid
from tkinter import Text
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import W
from tkinter import END

from random import randint

from pathlib import Path

def reset():
    resd4.configure(text="")
    resd6.configure(text="")
    resd8.configure(text="")
    resd10.configure(text="")
    resd12.configure(text="")
    resd20.configure(text="")
    resd100.configure(text="")
    resdX.configure(text="")
    history.delete(1.0,END)
    history.insert(0.0,"       NOTE       \n------------------\nThis field records your latest rolls at its top.")


def diceRoll(n, entdn, moddn, resdn):
    output=0
    dielist=[]
    for _ in range (0, int(entdn)):
        dieroll=randint(1,n)
        dielist.append(dieroll)
        output+=dieroll
    output+=int(moddn)
    resdn.configure(text=output)
    history.insert(0.0, f"rolling {entdn}d{n}+{moddn}\n{output}={dielist}+{moddn}\n")


NAME = "DnDie Roller v1.0.2"

HEIGHT = 260
WIDTH = 336

body=Tk()

body.iconbitmap(Path('.','d20.ico'))

body.minsize(179, 264)

body.title(NAME)


content= Canvas(body, height=HEIGHT, width=WIDTH)
content.pack()

divider= Frame(body, bg="gray")
divider.place(x=179, rely=0.5, y=-19, width=1 , relheight=1, anchor='center')

divider1= Frame(body, bg="gray")
divider1.place(relx=0.5, rely=1, y=-18, relwidth=1 , height=1, anchor='s')

container = Frame(body, bg="white")
container.place(relx=0, x=5, rely=0, y=5, width=169, relheight=1, height=-29, anchor='nw')

container2 = Frame(body)
container2.place(relx=0, x=185, rely=0, y=5, relwidth=1, width=-190, relheight=1, height=-29, anchor='nw')

history=Text(container2)
history.insert(0.0,"       NOTE       \n------------------\nThis field records your latest rolls at its top.")
history.place(relwidth=1, relheight=1, anchor='nw')

clear = Button(body,text="[clear]", command= lambda: reset(),bd=-3)
clear.place(rely=1, y=-18, x= 179, anchor='nw')





#bottom right label
info = Label(body, text=NAME,bd=-1)
info.place(relx=1, rely=1, anchor='se')

owner = Label(body, text="copyright or some shabbaz",bd=-1)
owner.place(relx=0, rely=1, anchor='sw')

#entry field templates

#one = StringVar(container, value='1') aka (xdX)
#zero = StringVar(container, value='+0') aka (ydX)

#table headers
#info: number, dice, roll, modifier, result

infnbr = Label(container, text="No.")
infnbr.grid(column=0,row=0,padx=(2,0),pady=2)

infdie = Label(container, text="Die",width=4)
infdie.grid(column=1, columnspan=2,row=0,padx=(2,0),pady=2)

infroll = Label(container, text="Roll")
infroll.grid(column=3,row=0,padx=(2,0),pady=2)

infmod = Label(container, text="Mod.")
infmod.grid(column=4,row=0,padx=(2,0),pady=2)

infres = Label(container, text="Result")
infres.grid(column=5,row=0,padx=(2,0),pady=2)


#d4 formatting
#initialising entries
xd4 = StringVar(container, value='1')
yd4 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d4

entd4= Entry(container, bg="white", width=2, justify='center',textvariable=xd4)
entd4.grid(column=0,row=1,padx=(2,0),pady=2)

infd4= Label(container, text="d4", bg="white")
infd4.grid(column=1, columnspan=2, row=1,padx=(2,0),pady=2,sticky=W)

btnd4 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(4,int(entd4.get()), int(modd4.get()),resdn=resd4))
btnd4.grid(column=3,row=1,padx=(2,0),pady=2)

modd4= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd4)
modd4.grid(column=4,row=1,padx=(2,0),pady=2)

resd4=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd4.grid(column=5,row=1,padx=(2,0),pady=2)


#d6 formatting
#initialising entries
xd6 = StringVar(container, value='1')
yd6 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d6

entd6= Entry(container, bg="white", width=2, justify='center',textvariable=xd6)
entd6.grid(column=0,row=2,padx=(2,0),pady=2)

infd6= Label(container, text="d6", bg="white")
infd6.grid(column=1, columnspan=2, row=2,padx=(2,0),pady=2,sticky=W)

btnd6 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(6,int(entd6.get()), int(modd6.get()),resdn=resd6))
btnd6.grid(column=3,row=2,padx=(2,0),pady=2)

modd6= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd6)
modd6.grid(column=4,row=2,padx=(2,0),pady=2)

resd6=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd6.grid(column=5,row=2,padx=(2,0),pady=2)


#d8 formatting
#initialising entries
xd8 = StringVar(container, value='1')
yd8 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d8

entd8= Entry(container, bg="white", width=2, justify='center',textvariable=xd8)
entd8.grid(column=0,row=3,padx=(2,0),pady=2)

infd8= Label(container, text="d8", bg="white")
infd8.grid(column=1, columnspan=2, row=3,padx=(2,0),pady=2,sticky=W)

btnd8 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(8,int(entd8.get()), int(modd8.get()),resdn=resd8))
btnd8.grid(column=3,row=3,padx=(2,0),pady=2)

modd8= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd8)
modd8.grid(column=4,row=3,padx=(2,0),pady=2)

resd8=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd8.grid(column=5,row=3,padx=(2,0),pady=2)


#d10 formatting
#initialising entries
xd10 = StringVar(container, value='1')
yd10 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d10

entd10= Entry(container, bg="white", width=2, justify='center',textvariable=xd10)
entd10.grid(column=0,row=4,padx=(2,0),pady=2)

infd10= Label(container, text="d10", bg="white")
infd10.grid(column=1, columnspan=2, row=4,padx=(2,0),pady=2,sticky=W)

btnd10 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(10,int(entd10.get()), int(modd10.get()),resdn=resd10))
btnd10.grid(column=3,row=4,padx=(2,0),pady=2)

modd10= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd10)
modd10.grid(column=4,row=4,padx=(2,0),pady=2)

resd10=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd10.grid(column=5,row=4,padx=(2,0),pady=2)


#d12 formatting
#initialising entries
xd12 = StringVar(container, value='1')
yd12 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d12

entd12= Entry(container, bg="white", width=2, justify='center',textvariable=xd12)
entd12.grid(column=0,row=5,padx=(2,0),pady=2)

infd12= Label(container, text="d12", bg="white")
infd12.grid(column=1, columnspan=2, row=5,padx=(2,0),pady=2,sticky=W)

btnd12 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(12,int(entd12.get()), int(modd12.get()),resdn=resd12))
btnd12.grid(column=3,row=5,padx=(2,0),pady=2)

modd12= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd12)
modd12.grid(column=4,row=5,padx=(2,0),pady=2)

resd12=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd12.grid(column=5,row=5,padx=(2,0),pady=2)


#d20 formatting
#initialising entries
xd20 = StringVar(container, value='1')
yd20 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d20

entd20= Entry(container, bg="white", width=2, justify='center',textvariable=xd20)
entd20.grid(column=0,row=6,padx=(2,0),pady=2)

infd20= Label(container, text="d20", bg="white")
infd20.grid(column=1, columnspan=2, row=6,padx=(2,0),pady=2,sticky=W)

btnd20 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(20,int(entd20.get()), int(modd20.get()),resdn=resd20))
btnd20.grid(column=3,row=6,padx=(2,0),pady=2)

modd20= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd20)
modd20.grid(column=4,row=6,padx=(2,0),pady=2)

resd20=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd20.grid(column=5,row=6,padx=(2,0),pady=2)


#d100 formatting
#initialising entries
xd100 = StringVar(container, value='1')
yd100 = StringVar(container, value='+0')

#entry, info, button, modifier, result : d100

entd100= Entry(container, bg="white", width=2, justify='center',textvariable=xd100)
entd100.grid(column=0,row=7,padx=(2,0),pady=2)

infd100= Label(container, text="d100", bg="white")
infd100.grid(column=1, columnspan=2, row=7,padx=(2,0),pady=2,sticky=W)

btnd100 = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(100,int(entd100.get()), int(modd100.get()),resdn=resd100))
btnd100.grid(column=3,row=7,padx=(2,0),pady=2)

modd100= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=yd100)
modd100.grid(column=4,row=7,padx=(2,0),pady=2)

resd100=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resd100.grid(column=5,row=7,padx=(2,0),pady=2)


#dX formatting
#initialising entries
xdX = StringVar(container, value='1')
xdY = StringVar(container, value='X')
ydX = StringVar(container, value='+0')

#entry, info, button, modifier, result : dX

entdX= Entry(container, bg="white", width=2, justify='center',textvariable=xdX)
entdX.grid(column=0,row=8,padx=(2,0),pady=2)

infdX= Label(container, text="d", bg="white",)
infdX.grid(column=1, row=8,padx=(2,0),pady=2,sticky=W)

infdX1= Entry(container, bg="white", textvariable=xdY,width=2)
infdX1.grid(column=2, row=8,pady=2,sticky=W)

btndX = Button(container, text="roll",relief='groove',bd=-1, command= lambda: diceRoll(int(infdX1.get()),int(entdX.get()), int(moddX.get()),resdn=resdX))
btndX.grid(column=3,row=8,padx=(2,0),pady=2)

moddX= Entry(container, text="1", bg="white", width=3, justify='center',textvariable=ydX)
moddX.grid(column=4,row=8,padx=(2,0),pady=2)

resdX=Label(container, text="",bg="white", width = 4,justify='center',relief="groove")
resdX.grid(column=5,row=8,padx=(2,0),pady=2)





body.mainloop()

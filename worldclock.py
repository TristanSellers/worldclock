from datetime import datetime
from tkinter import *
import pytz
import time

root = Tk()
root.geometry("500x250")
root.resizable(0,0)
root.title('Digital Clock')


def times():
    home=pytz.timezone('America/Chicago')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clockUSA.config(text=current_time)
    name.config(text="Chicago")
    clockUSA.after(10, times)

    home=pytz.timezone('Europe/Dublin')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clockEU.config(text=current_time)
    name.config(text="Dublin")
    clockEU.after(10, times)

    home=pytz.timezone('Japan')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clockJAPAN.config(text=current_time)
    name.config(text="Tokyo")
    clockJAPAN.after(10, times)

    home=pytz.timezone('Australia/Sydney')
    local_time=datetime.now(home)
    current_time=local_time.strftime("%H:%M:%S")
    clockAUS.config(text=current_time)
    name.config(text="Sydney")
    clockAUS.after(10, times)
        
Label(root, text='Current times', font='calibri 20 bold').pack(side=BOTTOM)

name=Label(root, text='America',font=('times',20,'bold'))
name.place(x=30, y=5)
clockUSA=Label(root, font=('times',25,'bold'))
clockUSA.place(x=10, y=40)
nota=Label(root, text="Hours   Minutes   Seconds", font='times 10 bold')
nota.place(x=10, y=80)

name=Label(root, text='Europe', font=('times',20,'bold'))
name.place(x=330, y=5)
clockEU=Label(root, font=('times',25,'bold'))
clockEU.place(x=310, y=40)
nota=Label(root, text="Hours   Minutes   Seconds", font='times 10 bold')
nota.place(x=310, y=80)

name=Label(root, text='Japan', font=('times',20,'bold'))
name.place(x=30, y=105)
clockJAPAN=Label(root, font=('times',25,'bold'))
clockJAPAN.place(x=10, y=140)
nota=Label(root, text="Hours   Minutes   Seconds", font='times 10 bold')
nota.place(x=10, y=180)

name=Label(root, text='Australia', font=('times',20,'bold'))
name.place(x=330, y=105)
clockAUS=Label(root, font=('times',25,'bold'))
clockAUS.place(x=310, y=140)
nota=Label(root, text="Hours   Minutes   Seconds", font='times 10 bold')
nota.place(x=310, y=180)

times()


root.mainloop()



from tkinter import *

window = Tk()
calculate = ""

window.title("калькулятор")
window.geometry("500x500")
window.resizable(width=False , height=False)


frame = Frame(window, bg='#1798e3')
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

label = Label(frame, text="а на руинах во славу народа!", font=150)
label.place(x=10, y=10, width=470)

label1 = Label(frame, text="строй соцеалистический мир!", font=150)
label1.place(x=10, y=40, width=470)


buttons = []
Xb = 50
Yb = 300

for i in range(10):
    buttons.append(Button(frame, text=i, font=100, bg='#c2c8cc'))
    if i == 0:
        buttons[0].place(x=175, y=425, width=100, height=50,)
    else:
        buttons[i].place(x=Xb, y=Yb, width=80, height=80)
        Xb += 100
        if Xb > 300:
            Yb -= 100
            Xb = 50

MINUS = (Button(frame, text='+', font=100, bg='#36a362'))
MINUS.place(x=360, y=350, width=60, height=60)

PLUS = (Button(frame, text='-', font=100, bg='#36a362'))
PLUS.place(x=360, y=280, width=60, height=60)


window.mainloop()
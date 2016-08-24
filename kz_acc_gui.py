'''
Created on 14 апр. 2016 г.

@author: serav
'''
#импортим все
from tkinter import *


def calculate():
    
    a_val = acc.get()
    if len(a_val) == 20 and a_val != 'KZССБББХХХХХХХХХХХХХ':
        print(a_val)
        try:
            cc = 98 - int(a_val[4:]+'203500')%97
            if cc< 10:
                cc = str('0'+str(cc))
                print(cc)
                output.delete("0.0","end")
                output.insert("0.0",cc)
            else:
                output.delete("0.0","end")
                output.insert("0.0",cc)
        except Exception:
            output.delete("0.0","end")
            output.insert("0.0",'номер счета не соответствует формату')
    else:
        output.delete("0.0","end")
        output.insert("0.0",'номер счета не соответствует формату')
        

def clear(event):
    event.widget.delete(0,END)

def ret(event):
    calculate()

root = Tk()
root.title("расчет контрольного разряда номера счета Казахстан")
root.minsize(520,230)
root.resizable(width=False, height=False)

frame = Frame(root)
frame.grid()

acc = Entry(frame, width=30)
acc.insert(0,'KZССБББХХХХХХХХХХХХХ')
acc.bind('<Button-1>', clear)
acc.bind('<Return>', ret)
acc.grid(row=1,column=1,padx=(10,0))

a_lab = Label(frame, text="введите номер счета в формате KZССБББХХХХХХХХХХХХХ и нажмите РАССЧИТАТЬ").grid(row=2,column=1)
b_lab = Label(frame, text="где БББ - код банка и ХХХХХХХХХХХХХ - внутрибанковский номер счета").grid(row=3,column=1)

but = Button(frame, text="РАССЧИТАТЬ", command=calculate).grid(row=4, column=1, padx=(10,0))
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=2)
output.grid(row=5, columnspan=8)

root.mainloop()
'''
Created on 15 апр. 2016 г.

@author: serav
'''
#импортим все
from tkinter import *

from tkinter import messagebox            

class Quitter(Frame):                          
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = messagebox.askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)


def fetch():
    print ('Input => "%s"') % ent.get()              # get text
    #ent.delete('0', END)
    ent.insert(END, 'x')
    ent.insert(0, 'x')

root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')    
ent.pack(side=TOP, fill=X)          

ent.focus()                         
ent.bind('<Return>', (lambda event: fetch()))      
btn = Button(root, text='Fetch', command=fetch)    
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()

    
    

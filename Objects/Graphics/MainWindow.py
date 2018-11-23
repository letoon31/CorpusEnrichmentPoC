from tkinter import Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
from tkinter import LEFT, GROOVE, RIGHT, Y, END, BOTTOM, TOP, DISABLED, X
from tkinter import Frame
from tkinter import Text

class MainWindow(Tk):
    def __init__(self, orchestra, title = "Chat"):
        super().__init__()
        self.orchestra = orchestra
        
        self.title(title)
        
        self.init_UI()
        
        self.input_field.bind("<Return>", self.user_message)

    def init_UI(self):
        self.frame = Frame(self, width=500, height=300)
        self.frame.pack_propagate(False)
        self.frame.grid(row=0, column=0, rowspan = 3, columnspan = 2)
        
        self.text = Text(self.frame)
        self.text.pack()
        
        self.input_user = StringVar()
        self.input_field = Entry(self, text = self.input_user)
        self.input_field.grid(row=3, column=0, columnspan=2, rowspan = 1)
        
        Button(self, text = "Show database").grid(row = 4, column = 0)
        Button(self, text = "Intents/Entities").grid(row = 4, column = 1)
        
    def user_message(self, event):
        question = self.input_field.get()
        print(question)
        self.text.insert(END, "\nUSER: " + question)
        
        self.input_user.set('')
        self.orchestra.ask_simple_question(question)
        
        return "break"
    
    def assistant_message(self, message):
        self.text.insert(END, "\nWATSON: " + message)

#from tkinter import *
#
#window = Tk()
#
#input_user = StringVar()
#input_field = Entry(window, text=input_user)
#input_field.pack(side=BOTTOM, fill=X)
#
#def enter_pressed(event):
#    input_get = input_field.get()
#    print(input_get)
#    label = Label(frame, text=input_get)
#    input_user.set('')
#    label.grid(row=1, column=1)
#    return "break"
#
#frame = Frame(window, width=300, height=300)
#frame.pack_propagate(False) # prevent frame to resize to the labels size
#input_field.bind("<Return>", enter_pressed)
#frame.pack()
#
#window.mainloop()
#
#exit()

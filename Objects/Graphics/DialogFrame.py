from tkinter import Frame
from tkinter import Text
from tkinter import END, Y, LEFT

class DialogFrame(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        
    def init_UI(self):
        self.text = Text(self)
        
        self.text.pack(side=LEFT, fill=Y)
        
        self.text.insert(END, "Hi !")
from tkinter import *
from tkinter.font import *
from components.buttons import BackButton


class Game(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.difficulty = StringVar()

        self.title = Label(self, textvariable=self.difficulty, font=Font(size=50))
        self.title.pack()

        self.backButton = BackButton(self)
        self.backButton.pack()

    def backCommand(self):
        self.pack_forget()
        self.parent.Main.pack()
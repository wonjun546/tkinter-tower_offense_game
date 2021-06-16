from tkinter import *
from tkinter.font import *
from components.buttons import MainButton, BackButton, LevelButton
from game import Game


class LevelPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.blank = Frame(self, width=100)
        self.blank.grid(row=0, column=0)

        self.gameButton = BackButton(self)
        self.gameButton.grid(row=0, column=5, pady=10)

        self.title = Label(self, text="난이도", font=Font(size=50))
        self.title.grid(row=1, column=1, columnspan=3, pady=50)

        self.easyButton = LevelButton(self, "쉬움", lambda: self.command("쉬움"))
        self.mediumButton = LevelButton(self, "보통", lambda: self.command("보통"))
        self.hardButton = LevelButton(self, "어려움", lambda: self.command("어려움"))
        self.easyButton.grid(row=2, column=1, padx=10)
        self.mediumButton.grid(row=2, column=2, padx=10)
        self.hardButton.grid(row=2, column=3, padx=10)

    def command(self, difficulty):
        self.pack_forget()
        self.parent.Game = Game(self.parent)
        self.parent.Game.difficulty.set(difficulty)
        self.parent.Game.pack()

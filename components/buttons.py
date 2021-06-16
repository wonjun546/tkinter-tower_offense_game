from tkinter import *
from tkinter.font import *


class MainButton(Button):
    def __init__(self, parent, text, command, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self["font"] = Font(size=30)
        self["width"] = 10
        self["height"] = 2
        self["text"] = text
        self["command"] = command


class BackButton(Button):
    def __init__(self, parent, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self["font"] = Font(size=15)
        self["width"] = 4
        self["height"] = 2
        self["text"] = "메인으로"

        def command():
            self.parent.pack_forget()
            self.parent.parent.Main.pack()

        self["command"] = command


class LevelButton(MainButton):
    def __init__(self, parent, text, command, *args, **kwargs):
        MainButton.__init__(self, parent, text, command, *args, **kwargs)
        self.parent = parent
        self["width"] = 7
        self["height"] = 5
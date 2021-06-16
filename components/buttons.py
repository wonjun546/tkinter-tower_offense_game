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
        self.configure(font=Font(size=15), text="메인으로")
        self.configure(width=4, height=2)

        def command():
            self.parent.pack_forget()
            self.parent.parent.Main.pack()

        self.configure(command=command)


class LevelButton(MainButton):
    def __init__(self, parent, text, command, *args, **kwargs):
        MainButton.__init__(self, parent, text, command, *args, **kwargs)
        self.parent = parent
        self.configure(width=7, height=5)


class UnitButton(Button):
    def __init__(self, parent, unitnumber, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(text=str(unitnumber))
        self.configure(width=2, height=2)


class UpgradeButton(Button):
    def __init__(self, parent, param, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(text=param)
        self.configure(width=4, height=2)

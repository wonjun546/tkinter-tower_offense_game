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
            if type(self.parent).__name__ == "Game":
                self.parent.parent.Game.destroy()
            self.parent.parent.Main.pack()

        self.configure(command=command)


class LevelButton(MainButton):
    def __init__(self, parent, text, command, *args, **kwargs):
        MainButton.__init__(self, parent, text, command, *args, **kwargs)
        self.parent = parent
        self.configure(width=7, height=5)


class UnitButton(Button):
    def __init__(self, parent, unitId, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(text=str(unitId))
        self.configure(width=2, height=2)

        def command():
            diffMoney = int(self.parent.parent.money.get()[1:]) - int(
                self.parent.unitCosts[unitId - 1][1:]
            )
            if diffMoney >= 0:
                self.parent.parent.map.addUnit(unitId)
                self.parent.parent.money.set("$" + str(diffMoney))

        self.configure(command=command)


class UpgradeButton(Button):
    def __init__(self, parent, param, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(text=param)
        self.configure(width=4, height=2)

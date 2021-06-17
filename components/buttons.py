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
        self.unitId = unitId
        self.configure(text=str(unitId))
        self.configure(width=2, height=2)
        self.description = [
            "1) basic unit.\n  HP: 50, DPS: 2.5, range:200, speed: 5",
            "2) tanker unit.\n  HP: 300, speed: 5",
            "3) unknown unit.\n  HP: ?, speed: ?",
            "4) unknown unit.\n  HP: ?, speed: ?",
            "5) unknown unit.\n  HP: ?, speed: ?",
            "6) unknown unit.\n  HP: ?, speed: ?",
            "7) unknown unit.\n  HP: ?, speed: ?",
        ]

        def command():
            diffMoney = self.parent.parent.money.get() - self.parent.unitCosts[unitId - 1].get()
            if diffMoney >= 0:
                self.parent.parent.map.addUnit(unitId)
                self.parent.parent.money.set(diffMoney)

        self.configure(command=command)

    def mouseHoverIn(self, _):
        self.tip = self.parent.parent.map.create_text(
            10, 570, text=self.description[self.unitId - 1], anchor=W
        )

    def mouseHoverOut(self, _):
        self.parent.parent.map.delete(self.tip)


class UpgradeButton(Button):
    def __init__(self, parent, param, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(text=param)
        self.configure(width=4, height=2)

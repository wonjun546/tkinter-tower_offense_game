from tkinter import *
from tkinter.font import *
from map import Map
from components.buttons import BackButton, UnitButton, UpgradeButton


class Game(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.difficulty = StringVar()
        self.title = Label(self, textvariable=self.difficulty, font=Font(size=50), width=10)
        self.title.grid(row=0, column=0, columnspan=2)

        self.backButton = BackButton(self)
        self.backButton.grid(row=0, column=2)

        self.map = Map(self, width=1200, height=600, background="green")
        self.map.grid(row=1, column=0, columnspan=3)

        self.unitFrame = UnitFrame(self)
        self.unitFrame.grid(row=2, column=0)

        self.upgradeFrame = UpgradeFrame(self)
        self.upgradeFrame.grid(row=2, column=1)

        self.money = StringVar()
        self.money.set("$40")
        self.moneyLabel = Label(self, textvariable=self.money)
        self.moneyLabel.grid(row=2, column=2)


class UnitFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.configure(highlightbackground="black")
        self.configure(highlightthickness=1)
        self.parent = parent
        self.unitCost = ["$10", "$20", "$40", "$80", "$150", "$300", "$1000"]
        self.unitButtons = [UnitButton(self, i) for i in range(1, 8)]
        self.unitLabels = [Label(self, text=i) for i in self.unitCost]
        for (i, B, L) in zip(range(7), self.unitButtons, self.unitLabels):
            B.grid(row=0, column=i, padx=15, pady=(20, 0))
            L.grid(row=1, column=i, padx=15, pady=5)


class UpgradeFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.configure(highlightbackground="black")
        self.configure(highlightthickness=1)
        self.parent = parent
        self.upgradeParams = ["attack", "HP", "speed", "money"]
        self.upgradeCost = ["$100", "$100", "$100", "$100"]
        self.upgradeButtons = [UpgradeButton(self, i) for i in self.upgradeParams]
        self.upgradeLabels = [Label(self, text=i) for i in self.upgradeCost]
        for (i, B, L) in zip(range(7), self.upgradeButtons, self.upgradeLabels):
            B.grid(row=0, column=i, padx=20, pady=(20, 0))
            L.grid(row=1, column=i, padx=20, pady=5)

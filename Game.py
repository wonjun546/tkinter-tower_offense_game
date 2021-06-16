from tkinter import *
from tkinter.font import *
from components.buttons import BackButton, UnitButton, UpgradeButton


class Game(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topFrame = Frame(self)
        self.topFrame.pack()
        self.difficulty = StringVar()
        self.title = Label(
            self.topFrame, textvariable=self.difficulty, font=Font(size=50), width=10
        )
        self.title.pack(side=LEFT, expand=YES)

        self.backButton = BackButton(self.topFrame)
        self.backButton.pack(side=LEFT)

        self.map = Canvas(self, width=1200, height=600, background="red")
        self.map.pack()

        self.bottomFrame = Frame(self)
        self.bottomFrame.pack()
        self.unitFrame = UnitFrame(self.bottomFrame)
        self.unitFrame.pack(side=LEFT)

        self.upgradeFrame = UpgradeFrame(self.bottomFrame)
        self.upgradeFrame.pack(side=LEFT)


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

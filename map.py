from tkinter import *
from unit import Unit
from tower import Tower


class Map(Canvas):
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.unitList = []
        self.towerList = []

        # road
        self.create_line(
            0,
            450,
            200,
            400,
            600,
            500,
            900,
            375,
            300,
            225,
            600,
            100,
            1000,
            200,
            1200,
            150,
            width=100,
            capstyle=ROUND,
            fill="#613613",
        )
        # tower
        self.towerList.append(Tower(self, 1, (500, 375)))
        self.towerList.append(Tower(self, 1, (820, 520)))
        self.towerList.append(Tower(self, 1, (730, 240)))
        self.towerList.append(Tower(self, 1, (370, 80)))

    def addUnit(self, unitId):
        self.unitList.append(Unit(self, unitId))

    def nextFrame(self):
        for unit in self.unitList:
            unit.update()
        for tower in self.towerList:
            tower.update()
        self.parent.moneyLabel.configure(text=self.parent.money)
        self.after(20, self.nextFrame)
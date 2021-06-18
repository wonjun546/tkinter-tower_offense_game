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
            500,
            450,
            500,
            450,
            150,
            200,
            150,
            200,
            360,
            1100,
            360,
            1100,
            560,
            800,
            560,
            800,
            50,
            550,
            50,
            550,
            250,
            1200,
            250,
            
            width=40,
            capstyle=ROUND,
            fill="#613613",
        )
        # tower
        self.towerList.append(Tower(self, 1, (500, 80)))
        self.towerList.append(Tower(self, 1, (150,250)))
        self.towerList.append(Tower(self, 1, (400,200)))
        self.towerList.append(Tower(self, 1, (550,310)))
        self.towerList.append(Tower(self, 1, (750,420)))
        self.towerList.append(Tower(self, 1, (1000,510)))
        self.towerList.append(Tower(self, 1, (900,310)))
        self.towerList.append(Tower(self, 1, (750,200)))
        self.towerList.append(Tower(self, 1, (100,450)))
        self.towerList.append(Tower(self, 1, (1100,200)))

    def addUnit(self, unitId):
        self.unitList.append(Unit(self, unitId))

    def nextFrame(self):
        for unit in self.unitList:
            unit.update()
        for tower in self.towerList:
            tower.update()
        self.parent.moneyLabel.configure(text=self.parent.money)
        self.after(20, self.nextFrame)

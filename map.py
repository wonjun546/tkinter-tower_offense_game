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
        self.towerList.append(Tower(self, 1, (500, 400)))

    def addUnit(self, unitId):
        print(unitId, "spawned")
        self.unitList.append(Unit(self, unitId))

    def nextFrame(self):
        for unit in self.unitList:
            unit.update()
        for tower in self.towerList:
            tower.update()
        self.after(20, self.nextFrame)
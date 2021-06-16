from tkinter import *


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

    def addUnit(self, unit):
        print(unit, "spawned")

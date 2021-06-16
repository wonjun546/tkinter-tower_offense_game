from .unit1 import Unit1
from .unit2 import Unit2


class Unit:
    def __init__(self, parent, unitId):
        if unitId == 1:
            self.unit = Unit1(self, parent)
        elif unitId == 2:
            self.unit = Unit2(self, parent)

    def update(self):
        self.unit.update()
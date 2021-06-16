from .baseUnit import baseUnit


class Unit2(baseUnit):
    def __init__(self, parent):
        baseUnit.__init__(self)
        self.parent = parent
        self.attack = 5
        self.attackRate = 2
        self.HP = 50
        self.speed = 1
        self.color = "blue"
        self.id = self.parent.create_oval(0, 475, 50, 425, fill=self.color)

    def update(self):
        dx, dy = self.nextPosition()
        self.parent.move(self.id, dx, dy)
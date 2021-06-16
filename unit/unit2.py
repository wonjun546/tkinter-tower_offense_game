from .baseUnit import baseUnit


class Unit2(baseUnit):
    def __init__(self, parent, canvas):
        baseUnit.__init__(self, canvas)
        self.parent = parent
        self.attack = 0
        self.attackRate = 0
        self.maxHP = 300
        self.HP = self.maxHP
        self.speed = 2
        self.color = "blue"
        self.id = self.canvas.create_oval(-25, 475, 25, 425, fill=self.color)

    def update(self):
        dx, dy = self.nextPosition()
        self.canvas.move(self.id, dx, dy)
        self.canvas.move(self.hpbar, dx, dy)
        self.canvas.move(self.hpbarBackground, dx, dy)
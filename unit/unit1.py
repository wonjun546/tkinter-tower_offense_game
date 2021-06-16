from .baseUnit import baseUnit


class Unit1(baseUnit):
    def __init__(self, parent, canvas):
        baseUnit.__init__(self, canvas)
        self.parent = parent
        self.attack = 5
        self.attackRate = 2
        self.maxHP = 50
        self.HP = self.maxHP
        self.speed = 5
        self.color = "red"
        self.id = self.canvas.create_oval(-25, 475, 25, 425, fill=self.color)

    def update(self):
        dx, dy = self.nextPosition()
        self.canvas.move(self.id, dx, dy)
        self.canvas.move(self.hpbar, dx, dy)
        self.canvas.move(self.hpbarBackground, dx, dy)
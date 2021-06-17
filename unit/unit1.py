from .baseUnit import baseUnit


class Unit1(baseUnit):
    def __init__(self, parent, canvas):
        baseUnit.__init__(self, canvas)
        self.parent = parent
        self.attack = 5
        self.attackRate = 0.5
        self.range = 300
        self.maxHP = 50
        self.HP = self.maxHP
        self.speed = 5
        self.color = "red"
        self.id = self.canvas.create_oval(-25, 475, 25, 425, fill=self.color)


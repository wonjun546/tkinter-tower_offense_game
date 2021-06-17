class baseTower:
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.inBattle = False
        self.x, self.y = pos[0], pos[1]
        self.hpbarBackground = canvas.create_rectangle(
            self.x - 25, self.y - 30, self.x + 25, self.y - 40, fill="gray"
        )
        self.hpbar = canvas.create_rectangle(
            self.x - 24, self.y - 31, self.x + 24, self.y - 39, fill="red"
        )

    def attacked(self, attack):
        if self.HP <= attack:
            self.HP = 0
            self.canvas.delete(self.id)
            self.canvas.delete(self.hpbar)
            self.canvas.delete(self.hpbarBackground)
            self.inBattle = False
            del self.canvas.towerList[self.canvas.towerList.index(self.parent)]
        else:
            self.HP -= attack
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 48
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attackAction(self, unit):
        if unit in self.canvas.unitList and self.HP > 0:
            unit.unit.attacked(self.attack)
            self.canvas.after(int(1000 * self.attackRate), lambda: self.attackAction(unit))
        else:
            self.inBattle = False

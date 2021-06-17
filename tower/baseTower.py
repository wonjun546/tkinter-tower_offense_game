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

    def update(self):
        if not self.inBattle:
            enemy = self.nearEnemy()
            if enemy != None:
                self.attackAction(self.canvas.unitList[enemy])

    def const(self):
        difficulty = self.canvas.parent.difficulty.get()
        if difficulty == "쉬움":
            return 3
        elif difficulty == "보통":
            return 2
        else:
            return 1

    def attacked(self, attack):
        if self.HP <= attack:
            self.HP = 0
            self.canvas.parent.money += self.maxHP * self.const() / 10
            self.canvas.delete(self.id)
            self.canvas.delete(self.hpbar)
            self.canvas.delete(self.hpbarBackground)
            self.inBattle = False
            del self.canvas.towerList[self.canvas.towerList.index(self.parent)]
        else:
            self.HP -= attack
            self.canvas.parent.money += attack * (self.const() - 1) / 5
            (x1, y1, x2, y2) = self.canvas.coords(self.hpbar)
            x2 = x1 + self.HP / self.maxHP * 48
            self.canvas.coords(self.hpbar, x1, y1, x2, y2)

    def attackAction(self, unit):
        if unit in self.canvas.unitList and self.HP > 0 and self.distance(unit.unit) < self.range:
            unit.unit.attacked(self.attack)
            self.canvas.after(int(1000 * self.attackRate), lambda: self.attackAction(unit))
        else:
            self.inBattle = False

    def distance(self, other):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        z1, w1, z2, w2 = other.canvas.coords(other.id)
        return 0.5 * ((x1 + x2 - z1 - z2) ** 2 + (y1 + y2 - w1 - w2) ** 2) ** 0.5

    def nearEnemy(self):
        if self.canvas.unitList:
            dist = [-1, self.range]
            for i in range(len(self.canvas.unitList)):
                unit = self.canvas.unitList[i].unit
                newdist = self.distance(unit)
                if newdist < dist[1]:
                    dist[1] = newdist
                    dist[0] = i
            if dist[0] != -1:
                self.inBattle = True
                return dist[0]

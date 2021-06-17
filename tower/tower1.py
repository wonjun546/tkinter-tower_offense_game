from .baseTower import baseTower


class Tower1(baseTower):
    def __init__(self, parent, canvas, pos):
        baseTower.__init__(self, canvas, pos)
        self.parent = parent
        self.attack = 10
        self.attackRate = 0.5
        self.range = 300
        self.maxHP = 300
        self.HP = self.maxHP
        self.id = canvas.create_rectangle(
            self.x - 25, self.y - 25, self.x + 25, self.y + 25, fill="yellow"
        )

    def update(self):
        if not self.inBattle:
            enemy = self.nearEnemy()
            if enemy != None:
                self.attackAction(self.canvas.unitList[enemy])

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

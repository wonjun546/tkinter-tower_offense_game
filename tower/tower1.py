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



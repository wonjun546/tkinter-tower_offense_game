def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


class baseUnit:
    def __init__(self, parent):
        self.road = [
            (0, 450),
            (200, 400),
            (600, 500),
            (900, 375),
            (300, 225),
            (600, 100),
            (1000, 200),
            (1200, 150),
        ]
        self.hpbarBackground = parent.create_rectangle(-25, 420, 25, 410, fill="gray")
        self.hpbar = parent.create_rectangle(-24, 419, 24, 411, fill="red")

    def nextPosition(self):
        if len(self.road) == 1:
            return (0, 0)
        (x1, y1, x2, y2) = self.parent.coords(self.id)
        _x, _y = (x1 + x2) / 2, (y1 + y2) / 2  # center
        x, y, length = _x, _y, self.speed
        if dist((_x, _y), self.road[1]) < self.speed:  # corner of road
            length -= dist((_x, _y), self.road[1])
            x, y = self.road[1]
            self.road.pop(0)
            if len(self.road) == 1:
                return (x - _x, y - _y)
        xvec = self.road[1][0] - self.road[0][0]
        yvec = self.road[1][1] - self.road[0][1]
        mag = (xvec ** 2 + yvec ** 2) ** 0.5
        x += xvec * length / mag  # x_1 = x_0 + dx
        y = yvec / xvec * (x - self.road[0][0]) + self.road[0][1]  # correction
        return (x - _x, y - _y)

    def attacked(self, attack):
        if self.HP <= attack:
            self.parent.destroy(self.id)
            self.parent.destroy(self.hpbar)
            self.parent.destroy(self.hpbarBackground)
            self.parent.unitList.remove(self)
        else:
            self.HP -= attack
            (x1, y1, x2, y2) = self.parent.coords(self.id)
            x2 = x1 + self.HP / self.maxHP * 48
            self.parent.coords(self.id, x1, y1, x2, y2)
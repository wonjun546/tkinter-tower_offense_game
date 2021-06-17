from .tower1 import Tower1


class Tower:
    def __init__(self, parent, towerId, pos):
        if towerId == 1:
            self.tower = Tower1(self, parent, pos)

    def update(self):
        self.tower.update()
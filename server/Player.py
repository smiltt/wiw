class Player:
    x = 0
    y = 0
    vx = 0
    vy = 0

    health = 10

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def intersects(self):


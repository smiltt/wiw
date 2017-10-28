class Object(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.health = 10

        self.width = 10
        self.height = 30

    x = 0
    y = 0
    vx = 0
    vy = 0

    health = 10

    width = 10
    height = 10

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

    def intersects(self, obj):
        return false

class Player(Object):

    shield_rot = 0

    def __init__(self):
        super(Player, self).__init__()

    def set_shield_rotation(self, rotation):
        self.shield_rot = rotation

    def get_shield_rotation(self):
        return self.shield_rot



class Alien(Object):

    gun_damage = 5

    def __init__(self, gun_dmg):
        super(Player, self).__init__()
        self.gun_damage = gun_dmg

    def fire(self):
        pass



class Projectile(Object):
    type = 0

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type
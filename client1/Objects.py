import pygame

class Object(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.health = 10

        self.width = 10
        self.height = 30

    x = 0
    y = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0

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
        return False

    def update(self, delta_t):
        pass

    def get_rect(self):
        return


class Player(Object):
    image = None
    shield_rot = 0
    image_frame = 0

    width = 80
    height = 120

    def __init__(self, image_path):
        super(Player, self).__init__
        self.set_image(image_path)

    def set_shield_rotation(self, rotation):
        self.shield_rot = rotation

    def get_shield_rotation(self):
        return self.shield_rot

    def update_frame(self):
        self.image_frame += 1

    def update(self, delta_t):
        self.x += self.vx * delta_t
        self.y += self.vy * delta_t
        self.vx += self.ax * delta_t
        self.vy += self.ay * delta_t

    def set_image(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path),(self.width, self.height))

    def get_image(self):
        return self.image

    def get_rect(self):
        return pygame.Rect((self.x,self.y), (self.width, self.height))


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
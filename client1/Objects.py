import pygame, math


class Object(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.health = 10

        self.width = 32
        self.height = 32

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
        if (
                        self.getX() < obj.getX() + obj.width and self.getX() + self.width > obj.getX() and self.getY() < obj.getY() + obj.height and self.getY() + self.height > obj.getY()):
            return True
        return False

    def update(self, delta_t):
        pass

    def get_rect(self):
        return

    def get(self):
        return self


class Wall(Object):
    x = 0
    y = 0
    width = 0
    height = 0
    color = (0, 0, 0)

    def __init__(self, x=0, y=0, width=0, height=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)

    def get_color(self):
        return self.color


class Player(Object):
    image = None
    shield_rot = 0
    image_frame = 0
    mov_speed = 1

    rotation = 0

    width = 32
    height = 32

    def __init__(self):
        super(Player, self).__init__
        self.images = [pygame.image.load("res/sprite1/mib00.png"),
                       pygame.image.load("res/sprite1/mib01.png"),
                       pygame.image.load("res/sprite1/mib02.png"),
                       pygame.image.load("res/sprite1/mib03.png"),
                       pygame.image.load("res/sprite1/mib04.png"),
                       pygame.image.load("res/sprite1/mib05.png"),
                       pygame.image.load("res/sprite1/mib06.png"),
                       pygame.image.load("res/sprite1/mib07.png"),
                       pygame.image.load("res/sprite1/mib08.png"),
                       pygame.image.load("res/sprite1/mib09.png"),
                       pygame.image.load("res/sprite1/mib10.png"),
                       pygame.image.load("res/sprite1/mib11.png"),
                       pygame.image.load("res/sprite1/mib12.png"),
                       pygame.image.load("res/sprite1/mib13.png"),
                       pygame.image.load("res/sprite1/mib14.png"),
                       pygame.image.load("res/sprite1/mib15.png")]
        self.current_image = 0

        self.image_count = len(self.images)

    def set_shield_rotation(self, rotation):
        self.shield_rot = rotation


    def set_mov_speed(self, val):
        self.mov_speed = val

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy

    def get_move_speed(self):
        return self.mov_speed

    def get_shield_rotation(self):
        return self.shield_rot

    def update_frame(self):
        self.image_frame += 1

    def update(self, delta_t):
        self.x += self.vx * delta_t
        self.y += self.vy * delta_t

    def de_update(self, delta_t):
        self.x -= self.vx * delta_t
        self.y -= self.vy * delta_t

    def set_image(self, no):
        self.image = pygame.transform.scale((self.images[self.current_image]), (self.width, self.height))

    def get_image(self):
        self.set_image(self.images[self.current_image])
        return self.image

    def get_rect(self):
        return pygame.Rect((self.x, self.y), (self.width + 64, self.height + 64))

    def update_rotation(self):
        if self.vx == 0 and self.vy > 0:
            self.rotation = 0
        elif self.vx == self.vy and self.vx > 0:
            self.rotation = 1
        elif self.vx > 0 and self.vy == 0:
            self.rotation = 2
        elif self.vx > 0 and self.vy < 0:
            self.rotation = 3
        elif self.vx == 0 and self.vy < 0:
            self.rotation = 4
        elif self.vx < 0 and self.vy < 0:
            self.rotation = 5
        elif self.vx < 0 and self.vy == 0:
            self.rotation = 6
        elif self.vx < 0 and self.vy > 0:
            self.rotation = 7


    def get_rotation(self):
        return self.rotation


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

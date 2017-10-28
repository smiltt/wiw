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
        return False

    def update(self, delta_t):
        pass

    def get_rect(self):
        return


class Player(Object):
    image = None
    shield_rot = 0
    image_frame = 0

    width = 120
    height = 120

    def __init__(self, image_path):
        super(Player, self).__init__
        images = [pygame.image.load("res/sprite1/mib00.png"),
                  pygame.image.load("res/sprite1/mib01.png"),
                  pygame.image.load("./res/sprite1/mib02.png"),
                  pygame.image.load("./res/sprite1/mib03.png"),
                  pygame.image.load("./res/sprite1/mib04.png"),
                  pygame.image.load("./res/sprite1/mib05.png"),
                  pygame.image.load("./res/sprite1/mib06.png"),
                  pygame.image.load("./res/sprite1/mib07.png"),
                  pygame.image.load("./res/sprite1/mib08.png"),
                  pygame.image.load("./res/sprite1/mib09.png"),
                  pygame.image.load("./res/sprite1/mib10.png"),
                  pygame.image.load("./res/sprite1/mib11.png"),
                  pygame.image.load("./res/sprite1/mib12.png"),
                  pygame.image.load("./res/sprite1/mib13.png"),
                  pygame.image.load("./res/sprite1/mib14.png"),
                  pygame.image.load("./res/sprite1/mib15.png")]
        self.current_image = images[0]
        self.set_image(self.current_image)

    def set_shield_rotation(self, rotation):
        self.shield_rot = rotation

    def set_player_rotation(self, ):
        return

    def get_shield_rotation(self):
        return self.shield_rot

    def update_frame(self):
        self.image_frame += 1

    def update(self, delta_t):
        if math.fabs(self.vx) < 0.2:
            self.vx = 0
        if math.fabs(self.vy) < 0.2:
            self.vy = 0

        self.x += self.vx * delta_t
        self.y += self.vy * delta_t
        self.vx += self.ax * delta_t ** 2
        self.vy += self.ay * delta_t ** 2

        self.ax = -0.2 * math.sqrt(self.vx ** 2 + self.vy ** 2) * self.vx
        self.ay = -0.2 * math.sqrt(self.vx ** 2 + self.vy ** 2) * self.vy

    def set_image(self, image_path):

        self.image = pygame.transform.scale((self.current_image), (self.width, self.height))

    def get_image(self):
        return self.image

    def get_rect(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))


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

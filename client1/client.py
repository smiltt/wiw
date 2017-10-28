import os, math, time, sys
import pygame.locals
import Objects

class Game:
    running = True
    screen = None
    player = Objects.Player()
    gameObjects = []
    t = time.time()
    level = None
    walls = []
    images = []
    player_time = 0
    player_anim_frame = 0


    def handle_keypress(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE]:
            self.player.set_mov_speed(2.5)
        else:
            self.player.set_mov_speed(1)

        if pressed[pygame.K_UP]:
            self.player.vy = self.player.get_move_speed()
        elif pressed[pygame.K_DOWN]:
            self.player.vy = -self.player.get_move_speed()
        else:
            self.player.vy = 0
        if pressed[pygame.K_RIGHT]:
            self.player.vx = -self.player.get_move_speed()
        elif pressed[pygame.K_LEFT]:
            self.player.vx = self.player.get_move_speed()
        else:
            self.player.vx = 0
        if (self.player.vx != 0 and self.player.vy != 0):
            self.player.vx = self.player.vx * 0.7
            self.player.vy = self.player.vy * 0.7


        if pressed[pygame.K_w]:
            pass
        if pressed[pygame.K_a]:
            pass
        if pressed[pygame.K_s]:
            pass
        if pressed[pygame.K_d]:
            pass

    def __init__(self):
        pygame.init()
        self.current_image = 0
        self.image_count = 15
        self.walls.append(Objects.Wall(0,50,200,10))
        self.walls.append(Objects.Wall(200,50,232,15))
        self.level = Map(16, 16)
        self.screen = pygame.display.set_mode((self.level.get_height() * 32, self.level.get_width() * 32))
        self.player = Objects.Player()
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

        #pygame.display.set_mode((1080, 720))

    def draw_player(self):
        if (self.player.get_vx() != 0 or self.player.get_vy() != 0):
            if (time.time() - self.player_time) > 0.02:
                print ("wtf")
                self.player_anim_frame += 1
                self.player_time = time.time()
                if self.player_anim_frame > self.image_count:
                    self.player_anim_frame = 0
        else:
            self.player_anim_frame = 0

        image = self.images[self.player_anim_frame]

        if (self.player.getX() != 0 or self.player.getY() != 0):
            if self.player.get_vy() == 0 and self.player.get_vx() == 1:
                image = pygame.transform.rotate(image, 90)
            if self.player.get_vy() == -1 and self.player.get_vx() == 0:
                image = pygame.transform.rotate(image, 180)
            if self.player.get_vy() == 0 and self.player.get_vx() == -1:
                image = pygame.transform.rotate(image, 270)

        self.screen.blit(image, self.player.get_rect())



    def draw(self):
        self.draw_map()
        self.current_image += 1
        self.draw_walls()
        self.draw_player()
        #print(self.image_count)
        #if self.current_image >= self.image_count:
            #self.current_image=0
        #print(self.current_image)
        #self.screen.blit(self.images[self.], self.player.get_rect())
        pygame.display.set_caption("Women in white")
        pygame.display.flip()

    def draw_walls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen, wall.get_color(), pygame.Rect(wall.get_rect()))


    def draw_map(self):
        tile = pygame.image.load('res/tile.png')

        for j in range(self.level.get_height()):
            for i in range(self.level.get_width()):
                self.screen.blit(tile, pygame.Rect((i*32, j*32), (32, 32)))

    def game_loop(self):
        self.player.setX(100)
        self.player.setY(200)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.handle_keypress()



            delta_t = (self.t - time.time()) * 10 ** (2)
            self.t = time.time()
            self.player.update(delta_t)
            for wall in self.walls:
                if self.player.intersects(wall):
                    self.player.de_update(delta_t)
                    print ("collided")
                    break

            for obj in self.gameObjects:
                obj.update(delta_t)

            self.draw()



def main():
    game = Game()
    game.game_loop()

class Map:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.set_dimensions(width, height)

    # size of level in tiles (16*16)
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    # return dimensions of map as tuple
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


main()



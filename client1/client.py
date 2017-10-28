import os, math, time, sys
import pygame.locals
from client1 import Objects

class Game:
    running = True
    screen = None
    player = None
    gameObjects = []
    t = time.time()
    level = None

    def handle_keypress(self):
        pass


    def __init__(self):
        pygame.init()

        self.level = Map(16, 16)
        self.screen = pygame.display.set_mode((self.level.get_height() * 16, self.level.get_width() * 16))
        self.player = Objects.Player('res/sprite1/Man In Black00.png')

        pygame.display.set_mode((1080, 720))

    def draw(self):
        self.draw_map()
        self.screen.blit(self.player.get_image(), self.player.get_rect())
        pygame.display.flip()

    def draw_map(self):
        tile = pygame.image.load('res/tile.png')

        for j in range(self.level.get_height()):
            for i in range(self.level.get_width()):
                pass
                #self.screen.blit(tile, pygame.Rect((i*16, j*16), (16, 16)))

    def game_loop(self):


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handle_keypress()
                elif event.type == pygame.QUIT:
                    sys.exit(0)

            delta_t = (self.t - time.time()) * 10 ** (-6)
            self.t = time.time()
            self.player.update(delta_t)
            for obj in self.gameObjects:
                obj.update(delta_t)

            self.draw()

    def main(self):
        gameObjects = []
        t = time.time()

        init()



        bums = True
        mapx = 500
        mapy = 500
        posx = []
        posy = []
        xp = 20
        yp = 20
        while bums == True:
            int(xp, yp, posx, posy)
            xp, yp = player.movep(xp, yp)

        def tile(posx, posy, T):
            for i in range(mapx):
                for n in range(mapy):
                    posx.append(16 + ((i - 1) * 16))
                    posy.append(16 + ((n - 1) * 16))


def int(xp, yp, posx, posy):
    screen = pygame.display.set_mode((1024, 768))
    thing = pygame.image.load('alien4.png')
    screen.blit(thing, (xp, yp))
    pygame.display.flip()
    tyle = pygame.image.load('tile.png')
    for i in posx:
        for n in posy:
            screen.blit(tyle, (posx(i), posy(n)))



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



import os,math,time,sys
import pygame.locals
from client1 import Objects, KeyHandler

global running
global screen
global player
running = True
screen = None
player = None


def int(xp, yp, posx, posy):
    screen = pygame.display.set_mode((1024, 768))
    thing = pygame.image.load('alien4.png')
    screen.blit(thing, (xp, yp))
    pygame.display.flip()
    tyle = pygame.image.load('tile.png')
    for i in posx:
        for n in posy:
            screen.blit(tyle, (posx(i), posy(n)))

def tile(posx, posy, T):
    for i in range(mapx):
        for n in range(mapy):
            posx.append(16 + ((i - 1) * 16))
            posy.append(16 + ((n - 1) * 16))


class player:
    def movep(xp, yp):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yp -= 1
                elif event.key == pygame.K_DOWN:
                    yp += 1
                elif event.key == pygame.K_RIGHT:
                    xp += 1
                elif event.key == pygame.K_LEFT:
                    xp -= 1
                    print("y")
        return xp, yp

def handle_keypress():


def init():
    pygame.init()

    this.level = Map(16,16)
    self.screen = pygame.display.set_mode(board.get_height()*16, board.get_width()*16)
    player = Objects.Player()

    pygame.display.set_mode(1080,720)



def draw():
    screen.fill("black")
    screen.blit(player.get_image(), player.get_rect())
    pygame.display.flip()


def main():
    gameObjects = []
    t = time.time()

    init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                handle_keypress()
            elif event.type == pygame.quit():
                sys.exit(0)

        delta_t = (t - time.time()) * 10**(-6)
        t = time.time()
        player.update(delta_t)
        for obj in gameObjects:
            obj.update(delta_t)





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

    

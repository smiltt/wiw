import threading
from client1 import net
import pygame

def main():
    connection = threading.Thread(net.init("127.0.0.1"))


    while 1:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            net.send_keypress(1)
        elif pressed[pygame.K_UP]:
            net.send_keypress(2)
        elif pressed[pygame.K_UP]:
            net.send_keypress(3)
        elif pressed[pygame.K_UP]:
            net.send_keypress(4)



main()
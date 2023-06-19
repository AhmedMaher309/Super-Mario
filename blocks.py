import pygame

from util import display

def get_image():
    image = "img/block.png"
    return pygame.image.load(image)

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = get_image()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.starting_y = self.y
        self.has_mushroom = False

    def draw(self):
        display.blit(self.image, (self.x, self.y))

import pygame

from util import display

def get_image():
    image = "img/castle.png"
    return pygame.image.load(image)

class Castle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = get_image()
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.starting_y = self.y
        self.needed_mushrooms = 0
        self.total_mushrooms = 0

    def draw(self):
        display.blit(self.image, (self.x, self.y))

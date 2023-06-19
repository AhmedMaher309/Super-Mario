import pygame

from util import display

def get_image():
    image = "img/mushroom.png"
    return pygame.image.load(image)

class Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = get_image()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.starting_y = self.y

    def draw(self):
        display.blit(self.image, (self.x, self.y))

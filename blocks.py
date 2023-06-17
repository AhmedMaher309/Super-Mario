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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jumping = False
        self.jump_speed = 2
        self.jump_height = 200
        self.starting_y = self.y

    def draw(self):
        display.blit(self.image, (self.x, self.y))
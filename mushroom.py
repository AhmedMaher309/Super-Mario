import pygame
import time
from util import display

def get_image():
    image = "img/mushroom.png"
    return pygame.image.load(image)

class Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = get_image()
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.starting_y = self.y
        self.moving_speed = 0.5


    def draw(self):
        display.blit(self.image, (self.x, self.y))

    def move_up(self):
        while self.y > self.starting_y - 80:
            self.y -= self.moving_speed

    def move_left(self):
        while self.x > 40:
            self.x -= self.moving_speed

import random
import pygame

from util import display


def get_image():
    image = "img/mario_stand.png"
    return pygame.image.load(image)

class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = get_image()
        self.image = pygame.transform.scale(self.image, (80, 120))
        self.jumping = False
        self.jump_speed = 2
        self.jump_height = 200
        self.starting_y = self.y

    def move_mario(self, dx, dy):
        self.x += dx
        self.y += dy

    def jump(self):
        self.current_y = self.y
        while self.y >= self.starting_y - self.jump_height:
            self.current_y -= self.jump_speed
            self.y = self.current_y
        self.jumping = False

    def return_back(self):
        while self.y < self.starting_y:
            self.y += self.jump_speed
        self.y = self.starting_y

    def draw(self):
        display.blit(self.image, (self.x, self.y))





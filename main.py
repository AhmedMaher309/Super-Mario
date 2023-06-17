import pygame
from util import display
from sound_effects import Sound_Effects, Background_Music

from Mario import Mario
from blocks import Block

FPS_CLOCK = pygame.time.Clock()
background_image = pygame.image.load("img/Untitled.png")
screen_width = 1800
screen_height = 900
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
Mario = Mario(5, 675)

blocks = []
x = 500
y = 400
for i in range(6):
    block = Block(x, y)
    blocks.append(block)
    if i > 1:
        x += 280
    else:
        x += 80


sound_effects = Sound_Effects()
background_music = Background_Music()
background_music.play()


def draw_blocks():
    for block in blocks:
        block.draw()
def update_mario_position(keys):
    if keys[pygame.K_RIGHT] and Mario.x < screen_width - 100:
        Mario.move_mario(10, 0)
    if keys[pygame.K_LEFT] and Mario.x > 5:
        Mario.move_mario(-10, 0)

def jump():
    Mario.jump()


running = True
while running:
    display.blit(background_image, (1, 0))
    Mario.draw()
    draw_blocks()
    keys = pygame.key.get_pressed()
    update_mario_position(keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                Mario.return_back()

    pygame.display.update()
    FPS_CLOCK.tick(60)

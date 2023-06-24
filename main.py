import pygame
from util import display
from sound_effects import Sound_Effects, Background_Music

from Mario import Mario
from blocks import Block
from mushroom import Mushroom
from castle import Castle


sound_effects = Sound_Effects()
background_music = Background_Music()
background_music.play()

FPS_CLOCK = pygame.time.Clock()
background_image = pygame.image.load("img/Untitled.png")
screen_width = 1850
screen_height = 900
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

Mario = Mario(5, 675)
castle = Castle(1400, 230)
castle.needed_mushrooms = 5
castle.total_mushrooms = 5

mushrooms = []
x = 490
y = 400
for i in range(5):
    mushroom = Mushroom(x, y)
    mushrooms.append(mushroom)
    if i > 1:
        x += 282
    else:
        x += 82

blocks = []
x = 500
y = 400
for i in range(5):
    block = Block(x, y)
    block.has_mushroom = True
    blocks.append(block)
    if i > 1:
        x += 282
    else:
        x += 82

def draw_blocks():
    for each_block in blocks:
        each_block.draw()

def draw_mushrooms():
    for each_mushroom in mushrooms:
        each_mushroom.draw()

def update_mario_position(keys):
    if keys[pygame.K_RIGHT] and Mario.x < screen_width - 100:
        Mario.move_mario(10, 0)
    if keys[pygame.K_LEFT] and Mario.x > 5:
        Mario.move_mario(-10, 0)

def jump():
    Mario.jump()

def check_blocks_collision(blocks):
    mario_rect = Mario.image.get_rect(topleft=(Mario.x, Mario.y))
    for each_block in blocks:
        block_rect = each_block.image.get_rect(topleft=(each_block.x, each_block.y))
        if mario_rect.colliderect(block_rect):
            if found_mushroom(each_block):
                print("Found mushroom")
                index = blocks.index(each_block)
                mushrooms[index].move_up()


def found_mushroom(block):
    if block.has_mushroom:
        return True
    return False

def is_winning_state():
    mario_rect = Mario.image.get_rect(topleft=(Mario.x, Mario.y))
    castle_rect = castle.image.get_rect(topleft=(castle.x+300, castle.y))
    if mario_rect.colliderect(castle_rect):
        print("You won!")
        image = pygame.image.load("img/won.jpg")
        background_image = pygame.transform.scale(image, (screen_width, screen_height))
        display.blit(background_image, (0, 0))
        pygame.display.update()
        background_music.stop()
        running = False

running = True
while running:
    display.blit(background_image, (1, 0))
    draw_mushrooms()
    draw_blocks()
    castle.draw()
    Mario.draw()
    keys = pygame.key.get_pressed()
    update_mario_position(keys)
    check_blocks_collision(blocks)
    is_winning_state()
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

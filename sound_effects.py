import pygame
pygame.mixer.init()

class Sound_Effects:
    def __init__(self):
        self.sound_effect = pygame.mixer.Sound('sound/main_sound.mp3')
        self.sound_effect.set_volume(0.5)

    def play(self):
        self.sound_effect.play()


class Background_Music:
    def __init__(self):
        pygame.mixer.music.load('sound/main_sound.mp3')
        pygame.mixer.music.set_volume(0.5)

    def play(self):
        pygame.mixer.music.play(-1)



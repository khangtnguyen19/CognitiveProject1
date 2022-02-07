import pygame
import random
import config
from pygame.locals import *


class Foot(pygame.sprite.Sprite):
    def __init__(self):
        super(Foot, self).__init__()
        foot = pygame.image.load("resources/feet1.png").convert_alpha()
        self.image = pygame.transform.scale(foot, (75, 75))
        self.rect = self.image.get_rect()

    def pos_update(self, pressed_mouses):
        mouse_pos = pygame.mouse.get_pos()
        if pressed_mouses[0]:
            self.rect = pygame.Rect(mouse_pos[0] - 25, mouse_pos[1] - 25, 75, 75)
        if self.rect.left < config.min_width:
            self.rect.left = config.min_width
        elif self.rect.right > config.max_width:
            self.rect.right = config.max_width
        if self.rect.top <= config.min_height:
            self.rect.top = config.min_height
        elif self.rect.bottom >= config.max_height:
            self.rect.bottom = config.max_height


class CloudNumber(pygame.sprite.Sprite):
    def __init__(self):
        super(CloudNumber, self).__init__()
        self.num = 0
        self.text = pygame.font.Font("freesansbold.ttf", 50)
        text_surface = self.text.render(str(self.num), True, (0, 0, 0))
        self.image = text_surface
        self.rect = text_surface.get_rect()

    def set_pos(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)

    def set_num(self, num):
        self.num = num
        self.image = self.text.render(str(self.num), True, (0, 0, 0))


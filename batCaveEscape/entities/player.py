import pygame
from config.settings import *


class Player:
    def __init__(self):
        self.image = pygame.image.load(
            "batCaveEscape/assets/imgs/bat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 40))

        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = HEIGHT // 2

        self.speed_y = 0

    def jump(self):
        self.speed_y = -JUMP_FORCE

    def update(self):
        self.speed_y += GRAVITY
        self.rect.y += self.speed_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision_bounds(self):
        return self.rect.top <= 0 or self.rect.bottom >= HEIGHT

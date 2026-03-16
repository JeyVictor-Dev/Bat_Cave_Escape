import pygame
import random
from config.settings import *


class Obstacle:
    def __init__(self, speed):
        self.speed = speed
        self.image = pygame.image.load(
            "assets/imgs/stalactite.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, 300))

        #  Posição do espaço entre obstáculos
        height = random.randint(200, HEIGHT - 200)

        #  Estalactite de cima
        self.top = self.image.get_rect(bottomleft=(
            WIDTH, height - SPACE_BETWEEN_OBSTACLES // 2))

        #  Estalactite de baixo
        self.bottom = self.image.get_rect(
            topleft=(WIDTH, height + SPACE_BETWEEN_OBSTACLES // 2))

        self.passed = False

    def update(self):
        self.top.x -= self.speed
        self.bottom.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.top)
        screen.blit(pygame.transform.flip(
            self.image, False, True), self.bottom)

    def check_collision(self, player_rect):
        return player_rect.colliderect(self.top) or player_rect.colliderect(self.bottom)

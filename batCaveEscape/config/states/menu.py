import pygame
from config.settings import *


class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("Lucia Sans Typewriter", 50, bold=True)
        self.font_text = pygame.font.SysFont("Lucia Sans Typewriter", 25)
        self.blink_timer = 0
        self.show_text = True

        #  Carregar logo
        self.logo = pygame.image.load(
            "batCaveEscape/assets/imgs/logo.png").convert_alpha()

        self.logo = pygame.transform.scale(self.logo, (450, 150))

    def draw(self, screen):
        screen.fill(BACKGROUND)

        #  Desenhar logo
        screen.blit(self.logo, (WIDTH // 2 - 225, 120))

        #  Texto iniciar
        self.blink_timer += 1

        if self.blink_timer > 30:
            self.show_text = not self.show_text
            self.blink_timer = 0

        if self.show_text:
            text_start = self.font_text.render(
                "Pressione SPACE para iniciar", True, TEXT)
            screen.blit(text_start, (WIDTH // 2 - 140, 350))

        #  Texto controles
        text_controls = self.font_text.render("SPACE = Voar", True, TEXT)
        screen.blit(text_controls, (WIDTH // 2 - 80, 400))

import pygame
from config.settings import *


class GameOver:

    def __init__(self):

        self.font_title = pygame.font.SysFont("Lucia Sans Typewriter", 60, bold=True)
        self.font_text = pygame.font.SysFont("Lucia Sans Typewriter", 30)

    def draw(self, screen, score):

        text_game_over = self.font_title.render("GAME OVER", True, TEXT)
        screen.blit(text_game_over, (WIDTH // 2 - 150, 200))

        text_score = self.font_text.render(f"Score {score}", True, TEXT)
        screen.blit(text_score, (WIDTH // 2 - 70, 300))

        text_restart = self.font_text.render(
            "Pressione R para reniciar", True, TEXT)
        screen.blit(text_restart, (WIDTH // 2 - 150, 350))

        text_menu = self.font_text.render(
            "Pressione ESC para voltar ao menu", True, TEXT)
        screen.blit(text_menu, (WIDTH // 2 - 190, 400))

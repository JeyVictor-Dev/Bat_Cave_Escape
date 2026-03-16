import pygame
from config.settings import *
from config.states.menu import Menu
from entities.player import Player
from entities.obstacle import Obstacle
from config.states.game_over import GameOver

#  Inicialização
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bat Cave Escape")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Lucia Sans Typewriter", 30)

#  Sons do jogo
pygame.mixer.init()
jump_sound = pygame.mixer.Sound("assets/sounds/jump.mp3")
hit_sound = pygame.mixer.Sound("assets/sounds/hit.wav")
score_sound = pygame.mixer.Sound("assets/sounds/score.wav")
game_over_sound = pygame.mixer.Sound(
    "assets/sounds/game_over.wav")

pygame.mixer.music.load("assets/sounds/music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#  Background do jogo
background = pygame.image.load(
    "assets/imgs/cave_background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#  Obstaculos
obstacles = []
obstacle_speed = SPEED_OBSTACLE

#  Jogador
player = Player()

#  Menu do jogo
state = "menu"
menu = Menu()
game_over_screen = GameOver()

#  Status do jogo
score = 0
game_over = False
count_frame = 0

#  Função Resetar jogo
def reset_game():
    global player, obstacles, score, game_over, obstacle_speed
    player = Player()
    obstacles = []
    score = 0
    game_over = False
    obstacle_speed = SPEED_OBSTACLE


#  Loop principal
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #  Eventos do Menu
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = "game"

        #  Eventos do Player
        if state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.jump()
                    jump_sound.play()

                if event.key == pygame.K_r and game_over:
                    reset_game()

        #  Eventos de tela de Game Over
        if state == "game_over":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    reset_game()
                    state = "game"

                if event.key == pygame.K_ESCAPE:
                    reset_game()
                    state = "menu"

    #  Lógica dos Obstaculos
    if state == "game":

        if not game_over:
            player.update()

        if count_frame % 90 == 0:
            obstacles.append(Obstacle(obstacle_speed))

        for obstacle in obstacles:
            obstacle.update()

            if obstacle.check_collision(player.rect) and not game_over:
                game_over = True
                state = "game_over"
                hit_sound.play()
                game_over_sound.play()
                pygame.mixer.music.set_volume(0.1)

            if obstacle.top.x < player.rect.x and not obstacle.passed:
                score += 1
                score_sound.play()
                obstacle_speed += INCREASE_DIFFICULTY
                obstacle.passed = True

        obstacles = [o for o in obstacles if o.top.x > -100]

        if player.check_collision_bounds():
            game_over = True
            state = "game_over"

        count_frame += 1

    #  Arte do jogo
    screen.blit(background, (0, 0))

    #  Desenhar Menu
    if state == "menu":
        menu.draw(screen)
    #  Desenhar Jogo
    if state == "game":

        player.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        text_score = font.render(f"Score: {score}", True, TEXT)
        screen.blit(text_score, (10, 10))

    #  Desenhar Game Over
    if state == "game_over":
        game_over_screen.draw(screen, score)

    pygame.display.update()

pygame.quit()

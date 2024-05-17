import os
import pygame
from .config import FONT_NAME, LEADERBOARD_FILE

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, (255, 255, 255))  # WHITE
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def create_bricks(rows, cols):
    from .sprites import Brick
    bricks = pygame.sprite.Group()
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * (60 + 10) + 35, row * (20 + 10) + 35)
            bricks.add(brick)
    return bricks

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as file:
            return [line.strip().split(' ') for line in file.readlines()]
    return []

def save_leaderboard(scores):
    with open(LEADERBOARD_FILE, 'w') as file:
        for name, score in scores:
            file.write(f"{name} {score}\n")

def show_leaderboard(screen, scores):
    screen.fill((0, 0, 0))  # BLACK
    draw_text(screen, "Leaderboard", 40, 400, 50)  # SCREEN_WIDTH // 2
    y = 150
    for name, score in scores:
        draw_text(screen, f"{name}: {score}", 30, 400, y)  # SCREEN_WIDTH // 2
        y += 50
    pygame.display.flip()
    pygame.time.wait(3000)

def game_over_screen(screen, score):
    draw_text(screen, "GAME OVER", 40, 400, 250)  # SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50
    draw_text(screen, f"Score: {score}", 30, 400, 300)  # SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    pygame.display.flip()
    pygame.time.wait(2000)

def get_player_name(screen):
    name = ""
    screen.fill((0, 0, 0))  # BLACK
    draw_text(screen, "Enter your name:", 30, 400, 250)  # SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return ""
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        screen.fill((0, 0, 0))  # BLACK
        draw_text(screen, "Enter your name:", 30, 400, 250)  # SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50
        draw_text(screen, name, 30, 400, 300)  # SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        pygame.display.flip()

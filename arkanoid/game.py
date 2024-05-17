import pygame
from .config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, hit_sound, lose_life_sound, game_over_sound
from .sprites import Paddle, Ball
from .utils import draw_text, create_bricks, load_leaderboard, save_leaderboard, show_leaderboard, game_over_screen, get_player_name

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Arkanoid Game")
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks(5, 10)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle)
    all_sprites.add(ball)
    all_sprites.add(bricks)

    score = 0
    lives = 3
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        if ball.lost:
            lives -= 1
            lose_life_sound.play()
            ball.reset()
            if lives == 0:
                game_over_sound.play()
                game_over_screen(screen, score)
                name = get_player_name(screen)
                if name:
                    leaderboard = load_leaderboard()
                    leaderboard.append((name, str(score)))
                    leaderboard = sorted(leaderboard, key=lambda x: int(x[1]), reverse=True)[:5]
                    save_leaderboard(leaderboard)
                    show_leaderboard(screen, leaderboard)
                running = False

        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed[1] = -ball.speed[1]
            hit_sound.play()

        hits = pygame.sprite.spritecollide(ball, bricks, True)
        for hit in hits:
            score

import pygame
from .config import paddle_image, ball_image, brick_image

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = paddle_image
        self.rect = self.image.get_rect()
        self.rect.centerx = 400  # SCREEN_WIDTH // 2
        self.rect.bottom = 580  # SCREEN_HEIGHT - 20
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = [5, -5]
        self.lost = False

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.left <= 0 or self.rect.right >= 800:  # SCREEN_WIDTH
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom >= 600:  # SCREEN_HEIGHT
            self.lost = True

    def reset(self):
        self.rect.center = (400, 300)  # (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = [5, -5]
        self.lost = False

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = brick_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

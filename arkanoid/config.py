import pygame
import os

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Asset paths
ASSET_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets')
SOUND_PATH = os.path.join(ASSET_PATH, 'sounds')
IMAGE_PATH = os.path.join(ASSET_PATH, 'images')
LEADERBOARD_FILE = os.path.join(ASSET_PATH, 'leaderboard.txt')

# Initialize Pygame
pygame.init()

# Load sounds
hit_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "hit.wav"))
lose_life_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "lose_life.wav"))
game_over_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "game_over.wav"))

# Load images
brick_image = pygame.image.load(os.path.join(IMAGE_PATH, "brick.png"))
paddle_image = pygame.image.load(os.path.join(IMAGE_PATH, "paddle.png"))
ball_image = pygame.image.load(os.path.join(IMAGE_PATH, "ball.png"))

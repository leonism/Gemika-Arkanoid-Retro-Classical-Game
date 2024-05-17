# arkanoid/__init__.py

from .config import *
from .game import main
from .sprites import Paddle, Ball, Brick
from .utils import *

__all__ = ["main", "Paddle", "Ball", "Brick"]

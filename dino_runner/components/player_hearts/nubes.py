import pygame
from dino_runner.utils.constants import (
    CLOUD
)
class Nubes:
    def __init__(self, x_position, y_position):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
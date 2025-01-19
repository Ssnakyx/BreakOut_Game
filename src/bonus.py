import random
import pygame

class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.bonus_type = bonus_type  # "expand" ou "extra_ball"
        self.color = (0, 255, 0) if bonus_type == "expand" else (0, 0, 255)
        self.falling_speed = 5
        self.active = True

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        if self.active:
            self.y += self.falling_speed

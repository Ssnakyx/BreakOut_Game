import random
import pygame

class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.bonus_type = bonus_type  # "expand" ou "extra_ball"
        self.color = (255, 255, 0) if bonus_type == "expand" else (0, 0, 255)
        self.falling_speed = 2
        self.active = True

    def draw(self, screen):
        """Dessine le bonus s'il est actif."""
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        """Met à jour la position du bonus et le désactive s'il sort de l'écran."""
        if self.active:
            self.y += self.falling_speed

        # Désactiver si le bonus sort de l'écran
        if self.y > 600:
            self.active = False

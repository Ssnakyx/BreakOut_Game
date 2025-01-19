import pygame
import time


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(350, 550, 100, 10)
        self.original_width = self.rect.width
        self.expanded_time = None  # Temps de début de l'agrandissement
        self.expanded_duration = 20  # Durée de l'agrandissement (en secondes)
        # self.color = (255, 255, 255)  # Couleur de la raquette
        # self.speed = 5  # Vitesse de déplacement

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        if self.expanded_time and time.time() - self.expanded_time >= self.expanded_duration:
            self.reset_width()
        
    def expand(self, extra_width):
        """Agrandit la largeur de la raquette pour une durée limitée."""
        if not self.expanded_time:  
            self.expanded_time = time.time() 
        self.rect.width = self.original_width
        self.rect.width += extra_width

        # S'assurer que la raquette reste à l'intérieur de l'écran
        self.rect.width = min(self.rect.width, 800)  # Limite maximale
        self.rect.x = min(self.rect.x, 800 - self.rect.width)
        
    def reset_width(self):
        """Réinitialise la largeur de la raquette à sa taille d'origine."""
        self.rect.width = self.original_width
        self.expanded_time = None  # Réinitialise le chronomètre
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
"""Test"""
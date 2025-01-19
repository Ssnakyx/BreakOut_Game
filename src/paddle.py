import pygame

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(350, 550, 100, 10)
        # self.color = (255, 255, 255)  # Couleur de la raquette
        # self.speed = 5  # Vitesse de déplacement

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        
    def expand(self, extra_width):
        # Augmente la largeur de la raquette
        self.rect.width += extra_width

        # S'assurer que la raquette reste à l'intérieur de l'écran
        self.rect.width = min(self.rect.width, 800)  # Limite maximale
        self.rect.x = min(self.rect.x, 800 - self.rect.width)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
"""Test"""
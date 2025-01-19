import pygame

class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load('data/img/brick.jpg')  # Charger l'image de la brique
        self.image = pygame.transform.scale(self.image, (width, height))  # Redimensionner l'image si nécessaire

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Afficher l'image de la brique

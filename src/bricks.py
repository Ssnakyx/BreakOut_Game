import pygame

class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load('data/img/brick.jpg')  
        self.image = pygame.transform.scale(self.image, (width, height)) 

    def draw(self, screen):
        screen.blit(self.image, self.rect)  

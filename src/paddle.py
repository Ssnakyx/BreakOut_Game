import pygame

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(350, 550, 100, 10)
        self.image = pygame.image.load('data/img/barre.jpg') 
        self.image = pygame.transform.scale(self.image, (100, 10))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))

    def draw(self, screen):
        screen.blit(self.image, self.rect) 

import pygame
import time


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(350, 550, 100, 10)
        self.image = pygame.image.load('data/img/barre.jpg') 
        self.image = pygame.transform.scale(self.image, (100, 10))
        self.original_width = self.rect.width
        self.expanded_time = None  
        self.expanded_duration = 20  
       

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        if self.expanded_time and time.time() - self.expanded_time >= self.expanded_duration:
            self.reset_width()
        
    def expand(self, extra_width):
        if not self.expanded_time:  
            self.expanded_time = time.time() 
        self.rect.width = self.original_width
        self.rect.width += extra_width

        self.rect.width = min(self.rect.width, 800) 
        self.rect.x = min(self.rect.x, 800 - self.rect.width)
        
    def reset_width(self):
        self.rect.width = self.original_width
        self.expanded_time = None  
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 

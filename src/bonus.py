import random
import pygame

class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.bonus_type = bonus_type
        self.active = True
        self.falling_speed = 2

     
        if bonus_type == "expand":
            self.image = pygame.image.load('data/img/coin.jpg') 
        elif bonus_type == "extra_ball":
            self.image = pygame.image.load('data/img/star.jpg')  
        else:
            self.image = None
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        if self.active and self.image:
            screen.blit(self.image, (self.x, self.y))

    def update(self):
        if self.active:
            self.y += self.falling_speed
        if self.y > 600:
            self.active = False

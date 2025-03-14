import pygame
from bonus import Bonus
import random

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(395, 295, 10, 10)
        self.vx = 4
        self.vy = -4
        self.image = pygame.image.load('data/img/ball.jpg') 
        self.image = pygame.transform.scale(self.image, (20, 20)) 

    def update(self, paddle, bricks, sounds, bonuses):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.vx *= -1

        if self.rect.top <= 0:
            self.vy *= -1

        if self.rect.colliderect(paddle.rect):
            self.vy *= -1
            if 'paddle_hit' in sounds:
                sounds['paddle_hit'].play() 

        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                self.vy *= -1
                if 'brick_break' in sounds:
                    sounds['brick_break'].play() 

                if random.random() < 0.20:
                    bonus_type = random.choice(["expand", "extra_ball"])
                    bonuses.append(Bonus(brick.rect.x + brick.rect.width // 2, brick.rect.y, bonus_type))
                break

        if self.rect.bottom >= 600:
            return False

        return True

    def draw(self, screen):
        screen.blit(self.image, self.rect) 

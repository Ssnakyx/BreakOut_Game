import pygame

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(395, 295, 10, 10)
        self.vx = 4
        self.vy = -4

    def update(self, paddle, bricks):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.vx *= -1
        if self.rect.top <= 0:
            self.vy *= -1

        if self.rect.colliderect(paddle.rect):
            self.vy *= -1

        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                self.vy *= -1
                break

        return self.rect.bottom < 600

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)

"""Test"""
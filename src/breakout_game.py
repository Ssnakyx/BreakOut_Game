import pygame

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(350, 550, 100, 10)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Empêche la palette de sortir de l'écran
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(395, 295, 10, 10)
        self.vx = 4
        self.vy = -4

    def update(self, paddle):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Collision avec les murs
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.vx *= -1
        if self.rect.top <= 0:
            self.vy *= -1

        # Collision avec la palette
        if self.rect.colliderect(paddle.rect):
            self.vy *= -1

        # Réinitialisation si la balle tombe en bas
        if self.rect.bottom >= 600:
            self.rect.x, self.rect.y = 395, 295
            self.vx, self.vy = 4, -4

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)

class BreakoutGame:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.paddle = None
        self.ball = None

    def initialize_game(self):
        """Initialise les composants du jeu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()

    def run_game(self):
        """Exécute la boucle principale du jeu"""
        self.initialize_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update(self.paddle)

            self.screen.fill((0, 0, 0))  # Remplit l'écran de noir
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()       # Met à jour l'affichage
            self.clock.tick(60)         # Limite la boucle à 60 FPS

        pygame.quit()

if __name__ == "__main__":
    game = BreakoutGame()
    game.run_game()

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

    def update(self, paddle, bricks):
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

        # Collision avec les briques
        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                self.vy *= -1
                break

        # Réinitialisation si la balle tombe en bas
        if self.rect.bottom >= 600:
            self.rect.x, self.rect.y = 395, 295
            self.vx, self.vy = 4, -4

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)

class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

class BreakoutGame:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.paddle = None
        self.ball = None
        self.bricks = []

    def initialize_game(self):
        """Initialise les composants du jeu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(5)]

    def run_game(self):
        """Exécute la boucle principale du jeu"""
        self.initialize_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update(self.paddle, self.bricks)

            self.screen.fill((0, 0, 0))  # Remplit l'écran de noir
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)

            for brick in self.bricks:
                brick.draw(self.screen)

            pygame.display.flip()       # Met à jour l'affichage
            self.clock.tick(60)         # Limite la boucle à 60 FPS

        pygame.quit()

if __name__ == "__main__":
    game = BreakoutGame()
    game.run_game()

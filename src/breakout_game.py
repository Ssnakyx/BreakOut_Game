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

        # Retourne False si la balle tombe en bas
        if self.rect.bottom >= 600:
            return False
        return True

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 0, 0), self.rect)

class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

class Menu:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.difficulty = 'medium'

    def initialize_menu(self):
        """Initialise les composants du menu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game - Menu")
        self.clock = pygame.time.Clock()

    def draw_menu(self):
        """Affiche le menu principal"""
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 74)
        title = font.render("Breakout Game", True, (255, 255, 255))
        self.screen.blit(title, (200, 100))

        button_font = pygame.font.Font(None, 50)
        play_button = button_font.render("Play", True, (0, 0, 0), (255, 255, 255))
        play_button_rect = play_button.get_rect(center=(400, 300))
        self.screen.blit(play_button, play_button_rect)

        difficulty_button = button_font.render(f"Difficulty: {self.difficulty}", True, (0, 0, 0), (255, 255, 255))
        difficulty_button_rect = difficulty_button.get_rect(center=(400, 400))
        self.screen.blit(difficulty_button, difficulty_button_rect)

        return play_button_rect, difficulty_button_rect

    def run_menu(self):
        """Exécute la boucle principale du menu"""
        self.initialize_menu()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.running = False
                        return self.difficulty  # Retourne la difficulté choisie
                    if self.difficulty_button_rect.collidepoint(event.pos):
                        # Cycle entre les difficultés
                        if self.difficulty == 'easy':
                            self.difficulty = 'medium'
                        elif self.difficulty == 'medium':
                            self.difficulty = 'hard'
                        else:
                            self.difficulty = 'easy'

            self.play_button_rect, self.difficulty_button_rect = self.draw_menu()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        return self.difficulty

class BreakoutGame:
    def __init__(self, difficulty):
        self.running = True
        self.screen = None
        self.clock = None
        self.paddle = None
        self.ball = None
        self.bricks = []
        self.difficulty = difficulty

    def initialize_game(self):
        """Initialise les composants du jeu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()

        # Génère les briques selon la difficulté
        if self.difficulty == 'easy':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(3)]
        elif self.difficulty == 'medium':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(5)]
        elif self.difficulty == 'hard':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(7)]

    def draw_game_over(self):
        """Affiche l'écran de fin de partie avec un bouton rejouer"""
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 74)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(game_over_text, (250, 200))

        button_font = pygame.font.Font(None, 50)
        replay_button = button_font.render("Replay", True, (0, 0, 0), (255, 255, 255))
        replay_button_rect = replay_button.get_rect(center=(400, 400))
        self.screen.blit(replay_button, replay_button_rect)

        pygame.display.flip()
        return replay_button_rect

    def run_game(self):
        """Exécute la boucle principale du jeu"""
        self.initialize_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            ball_active = self.ball.update(self.paddle, self.bricks)

            if not ball_active:  # Si la balle tombe, fin de partie
                replay_rect = self.draw_game_over()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if replay_rect.collidepoint(event.pos):
                                self.run_game()  # Relance le jeu
                                return

            self.screen.fill((0, 0, 0))  # Remplit l'écran de noir
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)

            for brick in self.bricks:
                brick.draw(self.screen)

            pygame.display.flip()       # Met à jour l'affichage
            self.clock.tick(60)         # Limite la boucle à 60 FPS

        pygame.quit()

if __name__ == "__main__":
    menu = Menu()
    selected_difficulty = menu.run_menu()
    game = BreakoutGame(selected_difficulty)
    game.run_game()

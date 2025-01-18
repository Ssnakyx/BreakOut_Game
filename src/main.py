import pygame
from paddle import Paddle
from ball import Ball
from bricks import Brick
import os

from ui import Menu

class BreakoutGame:
    def __init__(self, difficulty):
        self.running = True
        self.screen = None
        self.clock = None
        self.paddle = None
        self.ball = None
        self.bricks = []
        self.difficulty = difficulty
        self.sounds = {}

    def load_sounds(self):
        """Charge les effets sonores depuis le dossier sound"""
        sound_path = os.path.join("sound")  # Chemin vers le dossier sound
        self.sounds['paddle_hit'] = pygame.mixer.Sound("data/sound/Ball.mp3")#os.path.join(sound_path, "Ball.mp3"))
        self.sounds['brick_break'] = pygame.mixer.Sound("data/sound/brick.mp3")#os.path.join(sound_path, "brick.mp3"))

    def initialize_game(self):
        """Initialise les composants du jeu"""
        pygame.init()
        pygame.mixer.init()  # Initialisation pour les sons
        self.load_sounds()

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

    def run_game(self):
        """Exécute la boucle principale du jeu"""
        self.initialize_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            ball_active = self.ball.update(self.paddle, self.bricks, self.sounds)

            if not ball_active:  # Si la balle tombe, fin de partie
                print("Game Over!")
                self.running = False

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

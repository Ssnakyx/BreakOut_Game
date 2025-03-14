import pygame
import csv
from ui import Menu
from paddle import Paddle
from ball import Ball
from bricks import Brick
from bonus import Bonus
import os

from ui import Menu

class BreakoutGame:
    def __init__(self, difficulty):
        self.running = True
        self.screen = None
        self.clock = None
        self.paddle = None
        self.balls = None
        self.bricks = []
        self.difficulty = difficulty
        self.score = 0
        self.sounds = {}
        self.bonuses = []

    def load_sounds(self):
        sound_path = os.path.join("sound") 
        self.sounds['paddle_hit'] = pygame.mixer.Sound("data/sound/Ball.mp3")
        self.sounds['brick_break'] = pygame.mixer.Sound("data/sound/brick.mp3")

    def initialize_game(self):
        pygame.init()
        pygame.mixer.init() 
        self.load_sounds()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.balls = [Ball()]

        if self.difficulty == 'easy':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(3)]
        elif self.difficulty == 'medium':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(5)]
        elif self.difficulty == 'hard':
            self.bricks = [Brick(x * 80 + 5, y * 30 + 5, 70, 20) for x in range(10) for y in range(7)]

    def save_score(self):
        with open('score.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.score])

    def draw_game_over(self):
        self.screen.fill((0, 0, 0))

        font_title = pygame.font.Font(None, 74)
        game_over_text = font_title.render("Game Over", True, (255, 0, 0))
        self.screen.blit(game_over_text, (250, 150))

        font_score = pygame.font.Font(None, 50)
        score_text = font_score.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (300, 250))

        button_font = pygame.font.Font(None, 40)
        replay_button = button_font.render("Replay", True, (0, 0, 0), (255, 255, 255))
        replay_button_rect = replay_button.get_rect(center=(400, 350))
        pygame.draw.rect(self.screen, (50, 150, 50), replay_button_rect.inflate(20, 10), border_radius=10)
        self.screen.blit(replay_button, replay_button_rect)

        main_menu_button = button_font.render("Main Menu", True, (0, 0, 0), (255, 255, 255))
        main_menu_button_rect = main_menu_button.get_rect(center=(400, 450))
        pygame.draw.rect(self.screen, (150, 50, 50), main_menu_button_rect.inflate(20, 10), border_radius=10)
        self.screen.blit(main_menu_button, main_menu_button_rect)

        pygame.display.flip()
        return replay_button_rect, main_menu_button_rect

    def draw_victory_screen(self):
        self.screen.fill((0, 0, 0))

        font_title = pygame.font.Font(None, 74)
        victory_text = font_title.render("Victory!", True, (0, 255, 0))
        self.screen.blit(victory_text, (300, 150))

        font_score = pygame.font.Font(None, 50)
        score_text = font_score.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (300, 250))

        button_font = pygame.font.Font(None, 40)
        replay_button = button_font.render("Replay", True, (0, 0, 0), (255, 255, 255))
        replay_button_rect = replay_button.get_rect(center=(400, 350))
        pygame.draw.rect(self.screen, (50, 150, 50), replay_button_rect.inflate(20, 10), border_radius=10)
        self.screen.blit(replay_button, replay_button_rect)

        main_menu_button = button_font.render("Main Menu", True, (0, 0, 0), (255, 255, 255))
        main_menu_button_rect = main_menu_button.get_rect(center=(400, 450))
        pygame.draw.rect(self.screen, (150, 50, 50), main_menu_button_rect.inflate(20, 10), border_radius=10)
        self.screen.blit(main_menu_button, main_menu_button_rect)

        pygame.display.flip()
        return replay_button_rect, main_menu_button_rect

    def run_game(self):
        self.initialize_game()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            for ball in self.balls[:]:
                ball_active = ball.update(self.paddle, self.bricks, self.sounds, self.bonuses)
                if not ball_active:
                    self.balls.remove(ball)
            for bonus in self.bonuses[:]:
                bonus.update()
                if bonus.active and bonus.y + bonus.height >= self.paddle.rect.y:
                    if self.paddle.rect.colliderect(pygame.Rect(bonus.x, bonus.y, bonus.width, bonus.height)):
                        bonus.active = False
                        if bonus.bonus_type == "expand":
                            self.paddle.expand(50)
                        elif bonus.bonus_type == "extra_ball":
                            self.balls.append(Ball())
                elif not bonus.active:
                    self.bonuses.remove(bonus)

            if not self.balls:
                self.save_score()  
                replay_rect, main_menu_rect = self.draw_game_over()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if replay_rect.collidepoint(event.pos):
                                self.run_game() 
                                return
                            if main_menu_rect.collidepoint(event.pos):
                                return  

            if len(self.bricks) == 0:
                self.save_score()  
                replay_rect, main_menu_rect = self.draw_victory_screen()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if replay_rect.collidepoint(event.pos):
                                self.run_game()  
                                return
                            if main_menu_rect.collidepoint(event.pos):
                                return 
        
            self.screen.fill((0, 0, 0))
            self.paddle.draw(self.screen)
            for ball in self.balls:
                ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)
            for bonus in self.bonuses:
                bonus.draw(self.screen)
                
            self.score = (30 - len(self.bricks)) * 10
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    while True:
        menu = Menu()
        selected_difficulty = menu.run_menu()
        game = BreakoutGame(selected_difficulty)
        game.run_game()

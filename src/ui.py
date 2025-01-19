import pygame
import sys
import csv

class Menu:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.difficulty = 'easy'
        self.play_button_rect = None
        self.difficulty_button_rect = None
        self.scores_button_rect = None 

    def initialize_menu(self):
        """Initialise le menu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game - Menu")
        self.clock = pygame.time.Clock()

    def draw_rounded_button(self, text, rect, color, text_color, font, radius=20):
        pygame.draw.rect(self.screen, color, rect, border_radius=radius)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_description_box(self):
        box_rect = pygame.Rect(150, 450, 500, 100)
        pygame.draw.rect(self.screen, (50, 50, 50), box_rect, border_radius=15)
        pygame.draw.rect(self.screen, (200, 200, 200), box_rect, width=3, border_radius=15)


        font = pygame.font.Font(pygame.font.match_font("arial"), 20)
        text = [
            "The goal of Breakout is simple:",
            "Use the paddle to bounce the ball",
            "and break all the bricks without letting the ball fall."
        ]

        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(400, 460 + i * 25))
            self.screen.blit(text_surface, text_rect)

    def draw_menu(self):
        self.screen.fill((30, 30, 30))

        font_title = pygame.font.Font(pygame.font.match_font("arial", bold=True), 50)
        title = font_title.render("Breakout Game", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        button_font = pygame.font.Font(pygame.font.match_font("arial"), 30)

        self.play_button_rect = pygame.Rect(300, 200, 200, 50)
        self.draw_rounded_button("Play", self.play_button_rect, (50, 150, 50), (255, 255, 255), button_font)

        self.difficulty_button_rect = pygame.Rect(300, 300, 200, 50)
        self.draw_rounded_button(f"Difficulty: {self.difficulty}", self.difficulty_button_rect, (150, 50, 50), (255, 255, 255), button_font)

        self.scores_button_rect = pygame.Rect(300, 400, 200, 50)
        self.draw_rounded_button("View Scores", self.scores_button_rect, (50, 50, 150), (255, 255, 255), button_font)

        self.draw_description_box()

        return self.play_button_rect, self.difficulty_button_rect, self.scores_button_rect

    def show_scores(self):
        self.screen.fill((30, 30, 30))

        font_title = pygame.font.Font(pygame.font.match_font("arial", bold=True), 50)
        title = font_title.render("High Scores", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        try:
            with open('score.csv', mode='r') as file:
                reader = csv.reader(file)
                scores = sorted([int(row[0]) for row in reader], reverse=True)
        except FileNotFoundError:
            scores = []

        font_score = pygame.font.Font(pygame.font.match_font("arial"), 30)
        y_position = 200
        for idx, score in enumerate(scores[:10]): 
            score_text = font_score.render(f"{idx + 1}. {score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(400, y_position))
            self.screen.blit(score_text, score_rect)
            y_position += 40

        back_button_rect = pygame.Rect(300, y_position, 200, 50)
        self.draw_rounded_button("Back to Menu", back_button_rect, (150, 50, 50), (255, 255, 255), font_score)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_rect.collidepoint(event.pos):
                        return

    def run_menu(self):
        """Exécute le menu principal"""
        self.initialize_menu()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.running = False
                        return self.difficulty
                    if self.difficulty_button_rect.collidepoint(event.pos):
                        if self.difficulty == 'easy':
                            self.difficulty = 'medium'
                        elif self.difficulty == 'medium':
                            self.difficulty = 'hard'
                        else:
                            self.difficulty = 'easy'
                    if self.scores_button_rect.collidepoint(event.pos):
                        self.show_scores()

            self.play_button_rect, self.difficulty_button_rect, self.scores_button_rect = self.draw_menu()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        return self.difficulty

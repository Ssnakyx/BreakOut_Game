import pygame

class Menu:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.difficulty = 'medium'

    def initialize_menu(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game - Menu")
        self.clock = pygame.time.Clock()

    def draw_menu(self):
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
        self.initialize_menu()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.running = False
                        return self.difficulty
                    if self.difficulty_button_rect.collidepoint(event.pos):
                        self.difficulty = 'medium' if self.difficulty == 'easy' else ('hard' if self.difficulty == 'medium' else 'easy')

            self.play_button_rect, self.difficulty_button_rect = self.draw_menu()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        return self.difficulty

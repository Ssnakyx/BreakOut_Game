import pygame
import sys

class Menu:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = None
        self.difficulty = 'easy'
        self.play_button_rect = None
        self.difficulty_button_rect = None

    def initialize_menu(self):
        """Initialise le menu"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Breakout Game - Menu")
        self.clock = pygame.time.Clock()

    def draw_rounded_button(self, text, rect, color, text_color, font, radius=20):
        """Dessine un bouton avec des bords arrondis"""
        pygame.draw.rect(self.screen, color, rect, border_radius=radius)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_description_box(self):
        """Affiche une boîte contenant une description du jeu"""
        # Boîte
        box_rect = pygame.Rect(150, 450, 500, 100)
        pygame.draw.rect(self.screen, (50, 50, 50), box_rect, border_radius=15)
        pygame.draw.rect(self.screen, (200, 200, 200), box_rect, width=3, border_radius=15)

        # Texte
        font = pygame.font.Font(pygame.font.match_font("arial"), 20)
        text = [
            "The goal of Breakout is simple:",
            "Use the paddle to bounce the ball",
            "and break all the bricks without letting the ball fall."
        ]

        # Dessiner chaque ligne de texte
        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(400, 460 + i * 25))
            self.screen.blit(text_surface, text_rect)

    def draw_menu(self):
        """Affiche le menu principal"""
        self.screen.fill((30, 30, 30))  # Fond du menu

        # Titre
        font_title = pygame.font.Font(pygame.font.match_font("arial", bold=True), 50)
        title = font_title.render("Breakout Game", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        # Police pour les boutons
        button_font = pygame.font.Font(pygame.font.match_font("arial"), 30)

        # Bouton "Play"
        play_button_rect = pygame.Rect(300, 200, 200, 50)
        self.draw_rounded_button("Play", play_button_rect, (50, 150, 50), (255, 255, 255), button_font)

        # Bouton "Difficulty"
        difficulty_button_rect = pygame.Rect(300, 300, 200, 50)
        self.draw_rounded_button(f"Difficulty: {self.difficulty}", difficulty_button_rect, (150, 50, 50), (255, 255, 255), button_font)

        # Dessiner la boîte de description
        self.draw_description_box()

        return play_button_rect, difficulty_button_rect

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
                        # Cycle entre les difficultés
                        if self.difficulty == 'easy':
                            self.difficulty = 'medium'
                        elif self.difficulty == 'medium':
                            self.difficulty = 'hard'
                        else:
                            self.difficulty = 'easy'

            # Dessine le menu et met à jour les rectangles des boutons
            self.play_button_rect, self.difficulty_button_rect = self.draw_menu()

            # Met à jour l'affichage
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        return self.difficulty

# Test du menu
if __name__ == "__main__":
    menu = Menu()
    selected_difficulty = menu.run_menu()
    print(f"Difficulté sélectionnée : {selected_difficulty}")

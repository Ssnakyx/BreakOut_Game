class Menu:
    """
    Gère le menu principal du jeu. Cette classe contient des méthodes pour afficher
    les options du menu, gérer les sélections de l'utilisateur, et naviguer entre
    les différents écrans du jeu.
    """
    def __init__(self):
        pass

    def display_menu(self, screen):
        """Affiche le menu principal"""
        font = pygame.font.Font(None, 74)
        text = font.render("Breakout Game", True, (255, 255, 255))
        start_text = font.render("Press SPACE to Start", True, (255, 255, 255))

        screen.fill((0, 0, 0))
        screen.blit(text, (200, 150))
        screen.blit(start_text, (150, 300))
        pygame.display.flip()

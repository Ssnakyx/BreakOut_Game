import pygame

# Définition de la classe Brick
class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

# Classe pour générer les niveaux de difficulté
class DifficultyLevels:
    @staticmethod
    def generate_bricks(level):
        """Génère des niveaux de difficulté avec différentes dispositions de briques."""
        bricks = []
        if level == 'easy':
            bricks = [
                Brick(x * 80 + 5, y * 30 + 5, 70, 20)
                for x in range(10) for y in range(3)
            ]
        elif level == 'medium':
            bricks = [
                Brick(x * 80 + 5, y * 30 + 5, 70, 20)
                for x in range(10) for y in range(5)
            ]
        elif level == 'hard':
            bricks = [
                Brick(x * 80 + 5, y * 30 + 5, 70, 20)
                for x in range(10) for y in range(7)
            ]
        return bricks

# Exemple d'utilisation
if __name__ == "__main__":
    level = 'hard'  # Modifier ici pour tester les différents niveaux
    bricks = DifficultyLevels.generate_bricks(level)
    print(f"Généré {len(bricks)} briques pour le niveau {level}.")

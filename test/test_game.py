import pygame
from src.difficulty_levels import Paddle, Ball, Brick

def test_paddle_movement():
    paddle = Paddle()
    keys = pygame.key.get_pressed()

    # Simuler des touches pressées (aucune touche)
    paddle.update(keys)
    assert paddle.rect.x == 350, "Échec : La palette a bougé sans saisie utilisateur."

    # Simuler un déplacement vers la gauche
    keys = {pygame.K_LEFT: True}
    paddle.update(keys)
    assert paddle.rect.x < 350, "Échec : La palette ne bouge pas à gauche."

    print("Test de mouvement de la palette réussi.")

def test_ball_bounce():
    ball = Ball()
    ball.rect.x = 0
    ball.rect.y = 0
    ball.vx = -4
    ball.vy = -4

    # Simuler une collision avec le mur gauche
    ball.update(None, [])
    assert ball.vx > 0, "Échec : La balle ne rebondit pas sur le mur gauche."

    # Simuler une collision avec le mur haut
    ball.rect.y = 0
    ball.update(None, [])
    assert ball.vy > 0, "Échec : La balle ne rebondit pas sur le mur haut."

    print("Test de rebond de la balle réussi.")

def test_brick_collision():
    ball = Ball()
    brick = Brick(100, 100, 70, 20)
    ball.rect.x = 105
    ball.rect.y = 105
    bricks = [brick]

    # Simuler une collision avec une brique
    ball.update(None, bricks)
    assert brick not in bricks, "Échec : La brique n'a pas été retirée après une collision."

    print("Test de collision de la brique réussi.")

if __name__ == "__main__":
    pygame.init()
    test_paddle_movement()
    test_ball_bounce()
    test_brick_collision()
    print("Tous les tests ont été exécutés avec succès.")

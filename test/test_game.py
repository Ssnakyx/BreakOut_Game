import sys
sys.path.append('../src')
from difficulty_selection import DifficultySelection
from menu import Menu
from breakout_game import BreakoutGame

def test_menu():
    """Test du menu principal"""
    try:
        menu = menu()
        assert menu is not None
        print("test_menu passed")
    except AssertionError:
        print("test_menu failed")

def test_difficulty_selection():
    """Test de la sélection de la difficulté"""
    try:
        difficulty = DifficultySelection()
        assert difficulty.difficulty == "Medium"
        print("test_difficulty_selection passed")
    except AssertionError:
        print("test_difficulty_selection failed")

def test_game():
    """Test du jeu principal"""
    try:
        game = BreakoutGame()
        assert game.running is True
        print("test_game passed")
    except AssertionError:
        print("test_game failed")

if __name__ == "__main__":
    test_menu()
    test_difficulty_selection()
    test_game()

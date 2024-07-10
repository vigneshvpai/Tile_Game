import numpy as np
import MatrixAndColors  # Assuming MatrixAndColors is defined in matrix_and_colors.py


class Computer:
    def __init__(self, matrix_size: int, no_of_colors: int):
        self.game = MatrixAndColors.MatrixAndColors(matrix_size, no_of_colors)

    def play_game(self):
        self.game.set_colors()
        self.game.set_matrix()
        print("Initial State:")
        self.game.display()


if __name__ == "__main__":
    computer = Computer(matrix_size=5, no_of_colors=3)
    computer.play_game()

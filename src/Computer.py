import numpy as np
import MatrixAndColors  # Assuming MatrixAndColors is defined in matrix_and_colors.py
import time


class Computer:
    def __init__(self, matrix_size: int, no_of_colors: int):
        self.game = MatrixAndColors.MatrixAndColors(matrix_size, no_of_colors)

    def play_game(self):
        self.game.set_colors()
        self.game.set_matrix()
        self.game.display()

        while self.game.new_tiles_count < self.game.matrix_size * self.game.matrix_size:

            print("Computer is thinking ...\n")
            time.sleep(3)

            color_with_highest_reward = self.game.colors[-1]
            highest_reward = 0
            for color in self.game.colors:
                new_tiles_count = self.game.flood_fill(
                    (0, 0), color, modify_matrix=False
                )
                print(f"Reward for {color} is {new_tiles_count}\n")

                if new_tiles_count > highest_reward:
                    color_with_highest_reward = color

            print("Color choosen: ", color_with_highest_reward)
            new_tiles_count = self.game.flood_fill(
                (0, 0), color_with_highest_reward, modify_matrix=True
            )
            self.game.display()


if __name__ == "__main__":
    computer = Computer(matrix_size=5, no_of_colors=3)
    computer.play_game()

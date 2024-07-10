import numpy as np
import MatrixAndColors  # Assuming MatrixAndColors is defined in matrix_and_colors.py
import time


class Computer:
    def __init__(self, matrix_size: int, no_of_colors: int):
        self.game = MatrixAndColors.MatrixAndColors(matrix_size, no_of_colors)
        self.moves = []

    def play_game(self):
        self.game.set_colors()
        self.game.set_matrix()
        self.game.display()

        while True:

            print("Computer is thinking ...")
            time.sleep(1)

            new_color_list = np.unique(self.game.matrix)

            color_with_highest_reward = new_color_list[-1]
            highest_reward = 0

            for color in new_color_list:
                new_tiles_count = self.game.flood_fill(
                    (0, 0), color, modify_matrix=False
                )
                print(f"Reward for {color} is {new_tiles_count}")

                if new_tiles_count > highest_reward:
                    color_with_highest_reward = color

            print("Color choosen: ", color_with_highest_reward)
            new_tiles_count = self.game.flood_fill(
                (0, 0), color_with_highest_reward, modify_matrix=True
            )
            self.moves.append(color_with_highest_reward)
            if np.size(new_color_list) == 1:
                break
            self.game.display()

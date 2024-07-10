import MatrixAndColors
import Computer
import numpy as np


if __name__ == "__main__":

    matrix_size = int(input("Enter side length of square matrix: "))
    no_of_colors = int(input("Enter number of colors: "))

    matrix_and_colors = MatrixAndColors.MatrixAndColors(matrix_size, no_of_colors)
    matrix_and_colors.set_colors()
    matrix_and_colors.set_matrix()

    ans = input("Do you want to play? (Y/N): ")

    if ans == "Y":
        matrix_and_colors.display()
        while matrix_and_colors.new_tiles_count < np.square(
            matrix_and_colors.matrix_size
        ):
            next_color = int(input("Enter next color: "))
            print(
                "New tiles: ",
                matrix_and_colors.flood_fill((0, 0), next_color, modify_matrix=True),
            )
            matrix_and_colors.display()
    else:
        computer = Computer.Computer(matrix_size=matrix_size, no_of_colors=no_of_colors)
        computer.play_game()

        print()
        print("Best move: ", computer.moves[:-1])

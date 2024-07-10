import numpy as np


class MatrixAndColors:
    def __init__(self, matrix_size: int, no_of_colors: int):
        self.matrix_size = matrix_size
        self.no_of_colors = no_of_colors
        self.matrix = np.zeros((matrix_size, matrix_size), dtype=int)
        self.colors = np.zeros(no_of_colors, dtype=int)

    def set_colors(self):
        # Create a numpy list of numbers from 1 to no_of_colors
        self.colors = np.arange(1, self.no_of_colors + 1)

    def set_matrix(self):
        # Randomly assign color values to the elements of the matrix
        self.matrix = np.random.choice(
            self.colors, (self.matrix_size, self.matrix_size)
        )

    def display(self):
        # Display the matrix and colors
        print("Matrix:")
        print(self.matrix)
        print("Colors:")
        print(self.colors)


# Example usage:
matrix_size = 6
no_of_colors = 3

matrix_and_colors = MatrixAndColors(matrix_size, no_of_colors)
matrix_and_colors.set_colors()
matrix_and_colors.set_matrix()
matrix_and_colors.display()

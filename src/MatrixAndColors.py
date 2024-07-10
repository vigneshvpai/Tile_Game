import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


class MatrixAndColors:
    def __init__(self, matrix_size: int, no_of_colors: int):
        self.matrix_size = matrix_size
        self.no_of_colors = no_of_colors
        self.matrix = np.zeros((matrix_size, matrix_size), dtype=int)
        self.colors = np.zeros(no_of_colors, dtype=int)
        self.origin = (0, 0)
        self.new_tiles_count = 0  # Initialize count for new tiles

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

    def display_with_indices(self):
        # Display the matrix elements along with their indices
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                print(f"{self.matrix[i, j]}({i},{j})", end=" ")
            print()  # Newline after each row

    def flood_fill(self, index, new_value, modify_matrix):
        if new_value not in self.colors:
            raise ValueError("new_value must be a valid color from self.colors")
        start_row, start_col = index
        target_value = self.matrix[start_row, start_col]
        if target_value == new_value:
            return 0  # No need to fill if the target value is the same as the new value

        matrix = self.matrix if modify_matrix else self.matrix.copy()

        self.new_tiles_count = 0  # Reset new tiles count
        self._flood_fill_helper(matrix, start_row, start_col, target_value, new_value)
        return self.new_tiles_count  # Return the count of new tiles

    def _flood_fill_helper(self, matrix, row, col, target_value, new_value):
        if (
            row < 0
            or row >= self.matrix_size
            or col < 0
            or col >= self.matrix_size
            or matrix[row, col] != target_value
        ):
            return

        matrix[row, col] = new_value
        self.new_tiles_count += 1  # Increment count for each new tile added

        # Recursively apply flood fill to 4-connected neighbors
        self._flood_fill_helper(matrix, row + 1, col, target_value, new_value)
        self._flood_fill_helper(matrix, row - 1, col, target_value, new_value)
        self._flood_fill_helper(matrix, row, col + 1, target_value, new_value)
        self._flood_fill_helper(matrix, row, col - 1, target_value, new_value)

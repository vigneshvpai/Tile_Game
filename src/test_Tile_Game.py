import unittest
import numpy as np
import MatrixAndColors


class TestMatrixAndColors(unittest.TestCase):
    def test_initialization(self):
        n = 3
        m = 4
        matrix_and_colors = MatrixAndColors.MatrixAndColors(n, m)
        self.assertEqual(matrix_and_colors.matrix_size, n)
        self.assertEqual(matrix_and_colors.no_of_colors, m)
        self.assertTrue((matrix_and_colors.matrix == np.zeros((n, n), dtype=int)).all())
        self.assertTrue((matrix_and_colors.colors == np.zeros(m, dtype=int)).all())

    def test_set_colors(self):
        n = 3
        m = 4
        matrix_and_colors = MatrixAndColors.MatrixAndColors(n, m)
        matrix_and_colors.set_colors()
        self.assertTrue((matrix_and_colors.colors == np.arange(1, m + 1)).all())

    def test_set_matrix(self):
        n = 3
        m = 4
        matrix_and_colors = MatrixAndColors.MatrixAndColors(n, m)
        matrix_and_colors.set_colors()
        matrix_and_colors.set_matrix()
        for row in matrix_and_colors.matrix:
            for value in row:
                self.assertIn(value, matrix_and_colors.colors)

    def test_display(self):
        n = 3
        m = 4
        matrix_and_colors = MatrixAndColors.MatrixAndColors(n, m)
        matrix_and_colors.set_colors()
        matrix_and_colors.set_matrix()
        matrix_and_colors.display()  # This is a visual check; you should see the matrix and colors printed


if __name__ == "__main__":
    unittest.main()

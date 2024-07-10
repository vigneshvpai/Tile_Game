import MatrixAndColors

matrix_size = int(input("Enter side length of square matrix: "))
no_of_colors = int(input("Enter number of colors: "))

matrix_and_colors = MatrixAndColors.MatrixAndColors(matrix_size, no_of_colors)
matrix_and_colors.set_colors()
matrix_and_colors.set_matrix()
matrix_and_colors.display()

while True:
    next_color = int(input("Enter next color: "))
    print("New tiles: ", matrix_and_colors.flood_fill((0, 0), next_color))
    matrix_and_colors.display()

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for element in matrix:
        new_row = []

        for row in element:
            new_row.append(row ** 2)
        new_matrix.append(new_row)
    return new_matrix

# zero_matrix.py, zer_col_and_row takes an matrix input and if an element is 0, changes its row and col to 0

# TODO NOT DONE, gets the zeros indexes in to a list, needs to go through and change other items to zero based on that

matrix_1 = [[1, 2, 3, 4],
            [5, 0, 7, 0]]

matrix_2 = [[1, 2, 3, 4],
            [5, 6, 7, 8], 
            [1, 2, 3, 4]]

matrix_3 = [[0, 2, 3, 4],
            [5, 6, 7, 8], 
            [1, 2, 3, 4],
            [5, 6, 7, 0]]

def zer_col_and_row(matrix):
    # TODO include type check
    rows, columns = len(matrix), len(matrix[0])

    zeros = []
    # Search through each element
    for row in range(0, rows):
        for col in range(0, columns):
            # If zero, get index
            if matrix[row][col] == 0:
                zeros.append([row, col])

    # checks if zeros found, else returns input matrix
    if zeros:
        # Use the zero indexes to change other elements in rows  and cols (l) to 0 
        for row in range(0, rows):
            for col in range(0, columns):
                for zero in zeros:
                    if row == zero[0]:
                        matrix[row][col] = 0

                    if col == zero[1]:
                        matrix[row][col] = 0
 
        return matrix
    else:
        return matrix
        
    return rows, columns

print(zer_col_and_row(matrix_1))
print(zer_col_and_row(matrix_2))
print(zer_col_and_row(matrix_3))
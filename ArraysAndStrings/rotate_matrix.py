# rotate_matrix.py rotate_90 takes a list of list (matrix of N x N) input and rotates it by 90
# TODO rotate_90 has to be inefficient

matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def rotate_180(matrix):
    height, length = len(matrix), len(matrix[0])

    new_height = []
    for rh in range(height):
        new_height.insert(0, rh)

    new_length = []
    for rl in range(length):
        new_length.insert(0, rl)

    new_matrix = []
    for h in range(0, height):
        new_matrix.append([])
        for l in range(0, length):
            new_entry_height = new_height[h] 
            new_entry_length = new_length[l]
            new_matrix[h].append(matrix[new_entry_height][new_entry_length])

    return new_matrix


def rotate_90(matrix):
    height, length = len(matrix), len(matrix[0])

    new_temp_matrix = []
    for h in range(0, height):
        new_temp_matrix.append([])
        temp_list = []
        for l in range(0, length):
            temp_list.append(matrix[l][h])
            print(type(temp_list))
        new_temp_matrix.insert(h, (temp_list[::-1]))
    new_matrix = [x for x in new_temp_matrix if x != []]

    return new_matrix


print(rotate_90(matrix_1))
print(rotate_180(matrix_1))


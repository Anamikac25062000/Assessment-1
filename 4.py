# 4) Write a Python program to perform matrix multiplication using lists of lists.


matrix_A = [
    [2, 4, 6],
    [8, 10, 12],
]

matrix_B = [
    [1, 3],
    [5, 7],
    [9, 11],
]

if len(matrix_A[0]) != len(matrix_B):
    print("Matrices cannot be multiplied.")
else:
    result_matrix = [[0] * len(matrix_B[0]) for _ in range(len(matrix_A))]

    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    print("Result of Matrix Multiplication:")
    for row in result_matrix:
        print(row)

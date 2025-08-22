import numpy as np


# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# B = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# matrix = np.dot(A, B)
# print(matrix)


A = np.array([
    [1, 2],
    [3, 4]
])

A_inv = np.linalg.inv(A)
I = np.dot(A, A_inv)
print(np.linalg.det(I))
import numpy as np

# A = np.random.randint(1, 10, (3, 3))
# print("Двовимірний масив A:\n", A)

# # Транспонування
# A_transposed = A.T
# print("Транспонований масив:\n", A_transposed)

# # Одинична матриця
# identity_matrix = np.eye(3)
# print("Одинична матриця:\n", identity_matrix)

# # Матричний добуток
# matrix_product = np.dot(A, identity_matrix)
# print("Добуток A на одиничну матрицю:\n", matrix_product)


# A = np.arange(1, 13)
# print("Оригінальний масив A:", A)

# # Зміна форми масиву
# A_reshaped =  np.reshape(A, (3,4))
# print("Масив після reshape:\n", A_reshaped)

# # Транспонування
# A_transposed = np.transpose(A)
# print("Транспонований масив:\n", A_transposed)


# B = np.random.randint(1, 10, (2, 3, 4))
# print("Оригінальний тривимірний масив B:\n", B)

# # Перетворення у двовимірний масив
# B_reshaped = B.reshape((6,4))
# print("Масив після зміни форми:\n", B_reshaped)

# # Перетворення у одновимірний
# B_flattened = B.flatten()
# print("Одновимірний масив:\n", B_flattened)

# C = np.random.randint(1, 10, (3, 3, 3))
# print("Оригінальний масив C:\n", C)

# # Сума по першій осі
# sum_axis0 = C.sum(axis=0)
# print("Сума по осі 0:\n", sum_axis0)

# # Сума по другій осі
# sum_axis1 = C.sum(axis=1)
# print("Сума по осі 1:\n", sum_axis1)

# # Загальна сума
# total_sum = C.sum()
# print("Загальна сума елементів масиву:", total_sum)


# D = np.random.randint(10, 100, (4, 5))
# print("Оригінальний масив D:\n", D)

# # Середнє значення по кожному рядку
# row_mean = np.mean(D, axis=0)
# print("Середнє значення по рядках:", row_mean)

# # Максимальне значення по кожному стовпцю
# column_max = np.max(D, axis=0)
# print("Максимальні значення по стовпцях:", column_max)

# # Мінімальне значення в масиві
# overall_min = D.min()
# print("Мінімальне значення у всьому масиві:", overall_min)



sales_matrix = np.random.randint(10, 100, (4, 5))
print("Матриця продажів:\n", sales_matrix)

# Сума по рядках
row_sums = sales_matrix.sum(axis=0)
print("Суми по рядках:", row_sums)

# Сума по стовпцях
column_sums = sales_matrix.sum(axis=1)
print("Суми по стовпцях:", column_sums)
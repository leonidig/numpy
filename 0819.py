import numpy as np

array_3d = np.random.randint(-10, 10, size=(3, 4, 4))
print(f'{array_3d}\n')
array_after_deletion = np.delete(array_3d, 1, axis=0)
final_array = np.delete(array_after_deletion, -1, axis=2)

print("Остаточний масив після видалення:\n", final_array)
assert final_array.shape == (2, 4, 3), "Розмір масиву повинен бути (2, 4, 3)"
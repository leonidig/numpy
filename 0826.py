import numpy as np

# Створіть масив з випадкових чисел
array = np.random.randint(1, 10, size=5)
print(array)

# Створіть масив з rand()
rand_array = np.random.rand(5)
print(rand_array)

# Створіть масив з randint()
randint_array = np.random.randint(10, 20, size=5)
print(randint_array)

# Створіть масив з random()
random_array = np.random.random(5)
print(random_array)

# Створіть масив з normal()
normal_array = np.random.normal(0, 1, 5)
print(normal_array)

# Об'єднайте всі масиви
combined_array = np.concatenate([array, rand_array, randint_array, random_array, normal_array])
print(combined_array)

# Знайдіть середнє значення
average = np.mean(combined_array)
print(average)
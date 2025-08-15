import numpy as np


# array = np.random.randint(1, 21, size=15)
# indices = np.where(array % 2 == 0)

# print(f"Парні числа в масиві: {array[indices]}")

# assert isinstance(array, np.ndarray), "Об'єкт повинен бути масивом NumPy"
# assert len(array) == 15, "Масив повинен містити 15 елементів"
# assert np.all(array >= 1) and np.all(array <= 20), "Числа повинні бути від 1 до 20"


# ____________________________________________________________


# array = np.arange(16).reshape((4,4))
# indices = np.where(array % 3 == 0)
# print(f'{array}\n')
# array[indices] = -1
# print(array)


# ____________________________________________________________


# array = np.random.randint(10, 51, size=20)
# original_array = array.copy()
# indices = np.where((array >= 20) & (array <= 30))

# array [indices] = array[indices] ** 2
# print(f'{original_array}\n')
# print(array)


# ____________________________________________________________



# array = np.random.randint(1, 21, size = 14).reshape(7, 2)
# print(f'{array}\n')

# sorted_array = np.sort(array, axis=1)
# print(f'{sorted_array}\n')

# sorted_array_by_desc = np.sort(array)[::-1]
# print(f'{sorted_array_by_desc}\n')


# ____________________________________________________________


# array = np.random.randint(1, 21, size = 15)
# array_quicksort = np.sort(array, kind='quicksort')
# array_mergesort = np.sort(array, kind='mergesort')
# print(f'{array}\n{array_quicksort}\n{array_mergesort}')



# ____________________________________________________________


# array = np.array([
#     ('Alise', 25),
#     ('Bob', 20),
#     ('Charly', 30)
#     ], dtype=[('name', 'U10'), ('age', 'i4')])

# sorted_array = np.sort(array, order='age')
# print(sorted_array)


# ____________________________________________________________


# array = np.random.randint(1, 21, size=15)

# argsort_array = np.argsort(-array)
# sorted_array = array[argsort_array]

# print(sorted_array)



# ____________________________________________________________


# array = np.random.randint(1, 30, size=27).reshape(3, 3, 3)
# sorted_array = np.sort(array, axis=2)

# print(f'{array}\n')
# print(sorted_array)


# ____________________________________________________________


# array_names = np.array(['John', 'Bob', 'Carl', 'Alex'])
# array_grades = np.array([9, 2, 3, 2])

# indeces = np.lexsort((array_names, -array_grades))
# names_sorted = array_names[indeces]
# grades_soted = array_grades[indeces]


# ____________________________________________________________



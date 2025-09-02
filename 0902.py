import pandas as pd
import numpy as np


# data = {
#     'Ім’я': ['Анна', 'Богдан', 'Віктор'],
#     'Вік': [28, 34, 45],
#     'Місто': ['Київ', 'Львів', 'Одеса']
# }

# df = pd.DataFrame(data)
# print(df)

# _________________________________________________________________

# data = np.arange(1, 13).reshape(3, 4)
# df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# print(df)

# _________________________________________________________________

# data = {
#    'product': ['Laptop', 'Smartphone', 'Tablet'],
#    'price': [1200, 800, 400],
#    'stock': [50, 150, 200]
# }

# df = pd.DataFrame(data)
# print(df)

# _________________________________________________________________

# data = {
#     'name': ['Eve', 'Frank', 'Aboba'],
#     'age': [30, 45, 50],
#     'city': ['Berlin', 'Madrid', 'Rome']
# }

# df = pd.DataFrame(data)

# print(df)

# _________________________________________________________________

# data = [
#     ['John', 22, 88],
#     ['Alice', 23, 92],
#     ['Bob', 24, 75]
# ]

# df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])

# print(df)

# _________________________________________________________________

# data = np.array([
#     ('Ukraine', 3242342342, 10832119),
#     ('Germany', 93275461, 892472910),
#     ('Japan', 845782397, 93170411)

# ], dtype=[('Name', 'U10'), ('Population', 'i8'), ('Area', 'i8')])

# df = pd.DataFrame(data)
# print(df)

# _________________________________________________________________

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, 34, 29, 42],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }
# df = pd.DataFrame(data)
# row = df[df['Age'] > 30]
# print(row)

# _________________________________________________________________

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, 34, 29, 42],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }
# df = pd.DataFrame(data)
# filtered = df[(df['Age'] > 25) & (df['City'].isin(['Kyiv', 'Odessa']))]
# print(filtered)

# _________________________________________________________________


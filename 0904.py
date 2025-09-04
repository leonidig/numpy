import pandas as pd
import numpy as np



# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200.50, 800.75, 400.20],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)

# df['Price'] = df['Price'].astype('int64')

# print(df)


# --------------------------------------------------------------


# data = {
#     'Event': ['Conference', 'Meeting', 'Workshop'],
#     'Date': ['2024-05-21', '2024-06-15', '2024-07-10']
# }
# df = pd.DataFrame(data)

# df['Date'] = pd.to_datetime(df['Date'])

# print(df)


# --------------------------------------------------------------


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Department': ['HR', 'IT', 'Finance', 'IT'],
#     'Salary': [50000, 60000, 55000, 62000]
# }

# df = pd.DataFrame(data)

# df['Department'] = df['Department'].astype('category')

# print(df)


# --------------------------------------------------------------


# data = {
#     'Item': ['Book', 'Pen', 'Notebook'],
#     'Quantity': [10, 50, 30],
#     'Price': [15, 1, 5]
# }
# df = pd.DataFrame(data)

# df['Price'] = df['Price'].astype('float')


# --------------------------------------------------------------


# data = {
#     'Employee': ['John', 'Emma', 'Oliver'],
#     'Department': ['HR', 'Finance', 'IT'],
#     'Salary': [50000, 70000, 60000]
# }
# df = pd.DataFrame(data)

# df = df.rename(columns={
#     'Employee': 'Name',
#     'Salary': 'Income'
# })

# print(df)


# --------------------------------------------------------------

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, np.nan, 29, 42],
#     'City': ['Kyiv', 'Lviv', np.nan, 'Dnipro']
# }
# df = pd.DataFrame(data)
# print("Початковий DataFrame:")
# print(df)

# --------------------------------------------------------------


# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, np.nan, 29, 42],
#     'City': ['Kyiv', 'Lviv', np.nan, 'Dnipro']
# }
# df = pd.DataFrame(data)
# print("Початковий DataFrame:")
# print(df)

# clear_df = df.dropna()
# print(clear_df)

# --------------------------------------------------------------


# data = {
#     'Name': ['Lily', 'Mark', 'Nora', 'Diana'],
#     'Age': [26, 35, np.nan, 31],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }
# df = pd.DataFrame(data)

# mean_age = df['Age'].mean()

# df['Age'].fillna(mean_age)
# print(df)


# --------------------------------------------------------------


df = pd.read_csv('text.csv', dtype={''})
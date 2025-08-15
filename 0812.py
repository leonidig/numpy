import numpy as np
import time

# arr_int = np.array([1, 2, 3, 4, 5], dtype=int)
# arr_float = np.array([1.2, 3.4, 5.4, 4.20], dtype=float)
# arr_bool = np.array([True, True, False, True, False], dtype=bool)
# arr_complex = np.array([1+2j, 3+2j, 5+3j], dtype=complex)

# arr_int_32 = arr_int.astype(np.int32)
# arr_float_32 = arr_float.astype(np.float32)

# print(f'Array int32 = {arr_int_32}')
# print(f'Array int32 dtype {arr_int_32.dtype}')
# print(f'Array int32 bytes {arr_int_32.nbytes}')

# print(f'Array float32 = {arr_float_32}')
# print(f'Array float32 dtype {arr_float_32.dtype}')
# print(f'Array float bytes {arr_float_32.nbytes}')

# print(f'Array int = {arr_int}')
# print(f'Array int dtype {arr_int.dtype}')
# print(f'Array int bytes {arr_int.nbytes}')

# print(f'Array float = {arr_float}')
# print(f'Array float dtype {arr_float.dtype}')
# print(f'Array float bytes {arr_float.nbytes}')

# print(f'Array bool = {arr_bool}')
# print(f'Array bool dtype {arr_bool.dtype}')
# print(f'Array bool bytes {arr_bool.nbytes}')

# print(f'Array complex = {arr_complex}')
# print(f'Array complex dtype {arr_complex.dtype}')
# print(f'Array complex bytes {arr_complex.nbytes}')

# _____________________________________________________

# large_float64 = np.random.rand(1000000).astype(np.float64)
# large_float32 = large_float64.astype(np.float32)

# # print(f'{large_float64[:10]}\n\n{large_float32[:10]}')

# start = time.time()
# sum_float64 = large_float64.sum()
# end = time.time()

# print(f'Sum float64: {sum_float64}\nWasted time: {end-start}\n')


# start = time.time()
# sum_float32 = large_float32.sum()
# end = time.time()

# print(f'Sum float64: {sum_float32}\nWasted time: {end-start}')


# _____________________________________________________


# arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
# print(f'Dtype int = {arr.dtype}')

# arr_float = arr.astype(np.float32)
# print(f'Dtype float  = {arr_float.dtype}')

# arr_float_sum = arr_float.sum()
# print(f'Sum arr float = {arr_float_sum}')


# bool_arr = np.array([True, False, False, True], dtype=bool)
# print(bool_arr)
# print(bool_arr.dtype)


# _____________________________________________________


# int_arr = np.array([2, 4, 6, 8, 10], dtype=np.int32)
# complex64_arr = int_arr.astype(np.complex64)
# print(int_arr)
# print(int_arr.dtype)
# print(complex64_arr)
# print(complex64_arr.dtype)


# _____________________________________________________


# arr_int64 = np.arange(10000, dtype=np.int64)
# arr_int16 = np.arange(10000, dtype=np.int16)

# print(f'Arr int64: {arr_int64.nbytes}\nArr int16: {arr_int16.nbytes}')


# _____________________________________________________


# arr_int32 = np.arange(1, 1001, dtype=np.int32)
# print(arr_int32)
# print(arr_int32.dtype)

# arr_float32 = arr_int32.astype(np.float32)
# print(arr_int32)
# print(arr_int32.dtype)

# array = arr_float32 ** 2
# print(array)
# print(array.sum())


# _____________________________________________________


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array = np.array(matrix)
print(array, array[1, 2])
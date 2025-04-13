def mirror(arr):
    # mirrored_part = arr.reverse()  # mirrored_part == None, так как reverse изменит объект и ничего не вернет
    # arr = arr + mirrored_part  # Создаст новый объект, а не изменит исходный
    arr += arr[::-1]


arr = [1, 2, 3]
print(arr)
mirror(arr)
print(arr)

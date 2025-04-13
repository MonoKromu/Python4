nums = [3, 2, 1]
print('nums.sort()', id(nums), sep='\n')
nums.sort()
print(id(nums))  # Вызывается метод списка, объект остается тем же
nums = [3, 2, 1]
print('sorted(nums)', id(nums), sep='\n')
nums = sorted(nums)
print(id(nums))  # Создался новый список с помощью метода

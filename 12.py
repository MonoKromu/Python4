a = 3
b = 5
print('a = a + b', id(a), sep='\n')
a = a + b
print(id(a))
a = 3
print('a += b', id(a), sep='\n')
a += b
print(id(a))  # ID изменяется в обоих случаях, так как создается новый объект (неизменяемый тип данных)
l1 = [1, 2]
l2 = [3, 4, 5]
print('l1 = l1 + l2', id(l1), sep='\n')
l1 = l1 + l2
print(id(l1))
l1 = [1, 2]
print('l1 += l2', id(l1), sep='\n')
l1 += l2
print(id(l1))  # При += id остается тем же, так как изменяется существующий объект

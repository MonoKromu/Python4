# Код делит список чисел на список четных и список нечетных. В изначальном коде задания обе переменные хранили ссылку
# на один и тот же объект
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# odd = even = []
odd, even = [], []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)


print(odd)
print(even)

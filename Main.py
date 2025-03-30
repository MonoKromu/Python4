# №1
# numbers = [1, 2, 3, 4, 5, 8, 10, 13, 17, 25, 30, 60, 140]
# list_1 = [i for i in numbers if i < 5]
# list_2 = [i / 2 for i in numbers]
# list_3 = [i * 2 for i in numbers if i > 17]
# list_4 = [i * i for i in range(int(input()))]
# print(*[i * i for i in [int(i) for i in input().split()]])
# print(*[i for i in [j * j for j in [int(k) for k in input().split()] if j % 2 == 1] if i % 10 != 9])

# №2
# print("\n".join(i * '*' for i in [int(j) for j in input().split()]))

# №3
# def triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         print("Это треугольник")
#     else:
#         print("Это не треугольник")
#
#
# print(triangle(*[int(i) for i in input().split()]))

# №4
# def distance(x1, y1, x2, y2):
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
#
# print(distance(*[int(i) for i in input().split()]))

# №5
# def number_to_words(n):
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
#     words = """один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать
#     пятнадцать шестнадцать семнадцать восемнадцать девятнадцать давадцать тридцать сорок пятьдесят шестьдесят
#     семьдесят восемьдесят девяносто"""
#     n_to_w = dict(zip(numbers, words.split()))
#     if n <= 20:
#         return n_to_w[n]
#     elif n % 10 == 0:
#         return n_to_w[n - n % 10]
#     else:
#         return n_to_w[n - n % 10] + " " + n_to_w[n % 10]
#
#
# print(number_to_word(int(input)))

# №6
# def bracket_check(test_string: str):
#     signs = {'(': 1, ')': -1}
#     diff = 0
#     for i in test_string:
#         diff += signs.get(i, 0)
#         if diff < 0:
#             return 'NO'
#     if diff > 0:
#         return 'NO'
#     else:
#         return 'YES'
#
#
# print(bracket_check(input()))

# №7
# def palindrome(s: str):
#     s = s.lower().replace(' ', '')
#     if len([1 for i in range(int(len(s) / 2)) if s[i] != s[-i - 1]]) > 0:
#         return 'Не палиндром'
#     else:
#         return 'Палиндром'
#
#
# print(palindrome(int(input)))

# №8
# def tic_tac_toe(field):
#     l1, l2, l3 = field[0], field[1], field[2]
#     possible_wins = [(l1[0], l1[1], l1[2]), (l2[0], l2[1], l2[2]), (l3[0], l3[1], l3[2]),
#                      (l1[0], l2[0], l3[0]), (l1[1], l2[1], l3[1]), (l1[2], l2[2], l3[2]),
#                      (l1[0], l2[1], l3[2]), l1[2], l2[1], l3[0]]
#     if ('x', 'x', 'x') in possible_wins:
#         return 'x win'
#     elif ('0', '0', '0') in possible_wins:
#         return '0 win'
#     else:
#         return 'draw'
#
#
# print(tic_tac_toe([['0', '0', '0'], ['x', 'x', '0'], ['x', '-', 'x']]))

# №9
# messages = []
#
#
# def print_without_duplicates(message: str):
#     global messages
#     if message not in messages:
#         messages.append(message)
#         print(message)
#
#
# print_without_duplicates('Сообщение')
# print_without_duplicates('Сообщение')
# print_without_duplicates('Сообщение')
# print_without_duplicates('Доставлено')
# print_without_duplicates('Доставлено')
# print_without_duplicates('Успешно')

# №10
# friend_dict = {}
#
#
# def add_friends(name, friends):
#     if friend_dict.get(name) is None:
#         friend_dict[name] = friends
#     else:
#         friend_dict[name] += friends
#
#
# def are_friends(person1, person2):
#     return person2 in friend_dict[person1]
#
#
# def print_friends(name):
#     print(*sorted(friend_dict[name]))
#
#
# add_friends('Алла', ['Вова', 'Анна', 'Боб'])
# print(are_friends('Алла', 'Ваня'))
# add_friends('Алла', ['Ваня'])
# print(are_friends('Алла', 'Ваня'))
# print_friends('Алла')

# №11
# one = int(input())
# two = int(input())
# three = 0
#
#
# def roman(num):
#     rom = """- I II III IV V VI VII VIII IX X XX XXX XL L LX
#     LXX LXXX XC C CC CCC CD D DC DCC DCCC CM M MM MMM""".split()
#     if num > 3999:
#         return -1
#     else:
#         return ''.join([rom[i * 9 + (num // 10 ** i % 10)] for i in range(4) if (num // 10 ** i % 10) != 0][::-1])
#
#
# def roman_sum():
#     global three
#     three = one + two
#     print(f"{roman(one)} + {roman(two)} = {roman(three)}")
#
#
# roman_sum()

# №12
# a = 3
# b = 5
# print('a = a + b', id(a), sep='\n')
# a = a + b
# print(id(a))
# a = 3
# print('a += b', id(a), sep='\n')
# a += b
# print(id(a))  # ID изменяется в обоих случаях, так как создается новый объект (неизменяемый тип данных)
# l1 = [1, 2]
# l2 = [3, 4, 5]
# print('l1 = l1 + l2', id(l1), sep='\n')
# l1 = l1 + l2
# print(id(l1))
# l1 = [1, 2]
# print('l1 += l2', id(l1), sep='\n')
# l1 += l2
# print(id(l1))  # При += id остается тем же, так как изменяется существующий объект

# №13
# nums = [3, 2, 1]
# print('nums.sort()', id(nums), sep='\n')
# nums.sort()
# print(id(nums))  # Вызывается метод списка, объект остается тем же
# nums = [3, 2, 1]
# print('sorted(nums)', id(nums), sep='\n')
# nums = sorted(nums)
# print(id(nums))  # Создался новый список с помощью метода

# №14
# Код делит список чисел на список четных и список нечетных. В изначальном коде задания обе переменные хранили ссылку
# на один и тот же объект
# numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# # odd = even = []
# odd, even = [], []
# for number in numbers:
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#
#
# print(odd)
# print(even)

# №15
# fractal = [0, 1, 1, 2]
# fractal[1] = fractal
# fractal[2] = fractal
# print(fractal[1][1][1][1][1][1][1][1][1][0])

# №16
# def continue_fibonacci_sequence(sequence, n):
#     for i in range(n):
#         next_element = sequence[-1] + sequence[-2]
#         # sequence = sequence + [next_element]
#         sequence += [next_element]
#
#
# nums = [1, 1, 2]
# print(nums)
# continue_fibonacci_sequence(nums, 10)
# print(nums)

# №17
# def mirror(arr):
#     # mirrored_part = arr.reverse()  # mirrored_part == None, так как reverse изменит объект и ничего не вернет
#     # arr = arr + mirrored_part  # Создаст новый объект, а не изменит исходный
#     arr += arr[::-1]
#
#
# arr = [1, 2, 3]
# print(arr)
# mirror(arr)
# print(arr)

# №18
# def from_string_to_list(string, container):
#     container += [int(i) for i in string.split()]
#
#
# nums = [1, 5, 10]
# from_string_to_list(input(), nums)
# print(nums)

# №19
# def transpose(matrix):
#     transposed = [[] for _ in range(len(matrix))]
#     for i, line in enumerate(matrix):
#         for j in range(len(matrix[0])):
#             transposed[j].append(line[j])
#     matrix.clear()
#     for i, line in enumerate(transposed):
#         matrix.append(line)
#
#
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# transpose(mat)
# print(*mat, sep='\n')

# №20
# def swap(first, second):
#     first_copy = first[:]
#     first.clear()
#     for i in second:
#         first.append(i)
#     second.clear()
#     for i in first_copy:
#         second.append(i)
#
#
# f = ['sometext', 5, 3.14, True]
# s = [None, [1, 2, 3]]
# swap(f, s)
# print(f, s, sep='\n')

# №21
# def defractalize(fractal):
#     while fractal in fractal:
#         fractal.remove(fractal)
#
#
# fr = [0]
# fr.append(fr)
# defractalize(fr)
# print(fr)

# №22
# def fractal_print(fractal):
#     print([i for i in fractal])
#
#
# fr = []
# fr += [1, fr, 2, fr, 3]
# fractal_print(fr)

# №23
# def matrix(n=1, m=None, a=0):
#     if m is None:
#         m = n
#     return [[a for _ in range(m)] for i in range(n)]
#
#
# print(matrix())
# print(*matrix(3), sep='\n')
# print(*matrix(2, 4), sep='\n')
# print(*matrix(5, 5, 7), sep='\n')

# №24
# def partial_sums(*args):
#     return [sum(args[:i]) for i in range(len(args)+1)]
#
#
# print(partial_sums(1, 0.5, 0.25, 0.125, 0.0625))

# №25
# def solve(*coefficients):
#     length = len(coefficients)
#     if not 0 < length < 4:
#         return None
#     if length == 1 or (length == 2 and coefficients[0] == 0)
#     or (length == 3 and coefficients[0] == coefficients[1] == 0):
#         if coefficients[-1] == 0:
#             return ['all']
#         else:
#             return []
#     elif length == 2 or (length == 3 and coefficients[0] == 0):
#         if coefficients[-1] == 0:
#             return [0]
#         else:
#             return [coefficients[-1] / coefficients[-2]]
#     else:
#         a, b, c = coefficients[0], coefficients[1], coefficients[2]
#         d = b * b - (4 * a * c)
#         if d < 0:
#             return []
#         elif d == 0:
#             return [-b / (2 * a)]
#         else:
#             return [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]
#
#
# print(solve(*[int(i) for i in input().split()]))

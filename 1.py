numbers = [1, 2, 3, 4, 5, 8, 10, 13, 17, 25, 30, 60, 140]
list_1 = [i for i in numbers if i < 5]
list_2 = [i / 2 for i in numbers]
list_3 = [i * 2 for i in numbers if i > 17]
list_4 = [i * i for i in range(int(input()))]
print(*[i * i for i in [int(i) for i in input().split()]])
print(*[i for i in [j * j for j in [int(k) for k in input().split()] if j % 2 == 1] if i % 10 != 9])

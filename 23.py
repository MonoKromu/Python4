def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a for _ in range(m)] for i in range(n)]


print(matrix())
print(*matrix(3), sep='\n')
print(*matrix(2, 4), sep='\n')
print(*matrix(5, 5, 7), sep='\n')

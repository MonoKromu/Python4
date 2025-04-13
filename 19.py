def transpose(matrix):
    transposed = [[] for _ in range(len(matrix))]
    for i, line in enumerate(matrix):
        for j in range(len(matrix[0])):
            transposed[j].append(line[j])
    matrix.clear()
    for i, line in enumerate(transposed):
        matrix.append(line)


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
transpose(mat)
print(*mat, sep='\n')

def swap(first, second):
    first_copy = first[:]
    first.clear()
    for i in second:
        first.append(i)
    second.clear()
    for i in first_copy:
        second.append(i)


f = ['sometext', 5, 3.14, True]
s = [None, [1, 2, 3]]
swap(f, s)
print(f, s, sep='\n')

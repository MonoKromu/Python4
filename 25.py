def solve(*coefficients):
    length = len(coefficients)
    if not 0 < length < 4:
        return None
    if (length == 1 or (length == 2 and coefficients[0] == 0)
            or (length == 3 and coefficients[0] == coefficients[1] == 0)):
        if coefficients[-1] == 0:
            return ['all']
        else:
            return []
    elif length == 2 or (length == 3 and coefficients[0] == 0):
        if coefficients[-1] == 0:
            return [0]
        else:
            return [coefficients[-1] / coefficients[-2]]
    else:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        d = b * b - (4 * a * c)
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]


print(solve(*[int(i) for i in input().split()]))

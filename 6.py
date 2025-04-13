def bracket_check(test_string: str):
    signs = {'(': 1, ')': -1}
    diff = 0
    for i in test_string:
        diff += signs.get(i, 0)
        if diff < 0:
            return 'NO'
    if diff > 0:
        return 'NO'
    else:
        return 'YES'


print(bracket_check(input()))

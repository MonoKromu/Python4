def palindrome(s: str):
    s = s.lower().replace(' ', '')
    if len([1 for i in range(int(len(s) / 2)) if s[i] != s[-i - 1]]) > 0:
        return 'Не палиндром'
    else:
        return 'Палиндром'


print(palindrome(int(input)))

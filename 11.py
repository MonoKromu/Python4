one = int(input())
two = int(input())
three = 0


def roman(num):
    rom = """- I II III IV V VI VII VIII IX X XX XXX XL L LX
    LXX LXXX XC C CC CCC CD D DC DCC DCCC CM M MM MMM""".split()
    if num > 3999:
        return -1
    else:
        return ''.join([rom[i * 9 + (num // 10 ** i % 10)] for i in range(4) if (num // 10 ** i % 10) != 0][::-1])


def roman_sum():
    global three
    three = one + two
    print(f"{roman(one)} + {roman(two)} = {roman(three)}")


roman_sum()

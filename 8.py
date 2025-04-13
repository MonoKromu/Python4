def tic_tac_toe(field):
    l1, l2, l3 = field[0], field[1], field[2]
    possible_wins = [(l1[0], l1[1], l1[2]), (l2[0], l2[1], l2[2]), (l3[0], l3[1], l3[2]),
                     (l1[0], l2[0], l3[0]), (l1[1], l2[1], l3[1]), (l1[2], l2[2], l3[2]),
                     (l1[0], l2[1], l3[2]), l1[2], l2[1], l3[0]]
    if ('x', 'x', 'x') in possible_wins:
        return 'x win'
    elif ('0', '0', '0') in possible_wins:
        return '0 win'
    else:
        return 'draw'


print(tic_tac_toe([['0', '0', '0'], ['x', 'x', '0'], ['x', '-', 'x']]))

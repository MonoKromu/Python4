friend_dict = {}


def add_friends(name, friends):
    if friend_dict.get(name) is None:
        friend_dict[name] = friends
    else:
        friend_dict[name] += friends


def are_friends(person1, person2):
    return person2 in friend_dict[person1]


def print_friends(name):
    print(*sorted(friend_dict[name]))


add_friends('Алла', ['Вова', 'Анна', 'Боб'])
print(are_friends('Алла', 'Ваня'))
add_friends('Алла', ['Ваня'])
print(are_friends('Алла', 'Ваня'))
print_friends('Алла')

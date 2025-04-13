messages = []


def print_without_duplicates(message: str):
    global messages
    if message not in messages:
        messages.append(message)
        print(message)


print_without_duplicates('Сообщение')
print_without_duplicates('Сообщение')
print_without_duplicates('Сообщение')
print_without_duplicates('Доставлено')
print_without_duplicates('Доставлено')
print_without_duplicates('Успешно')

#Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user():
    answer = None
    while answer != 'Хорошо':
        answer = input('Как дела? ')

ask_user()
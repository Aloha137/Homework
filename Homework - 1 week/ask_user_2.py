#Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
#    Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
#    Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
#    При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”


def get_answer(question):
    question = str(question).lower()
    answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}
    print(answers[question])

def ask_user():
    question = None
    while question != 'Хорошо':
        question = input('Как дела? ')
        
        try:
            get_answer(question)
            except KeyError :
            print('Не знаю что сказать...')
        
        if question == 'пока':
            break

try:
    ask_user()
except KeyboardInterrupt:
    print('\nВсего хорошего!')
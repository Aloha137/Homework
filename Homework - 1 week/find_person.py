#Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()


def find_person(name):
    i = 0
#    index = 0
#    while name_list[index] != name:
#        index += 1
#    return name_list[index]
    while i != name:
        try:
            i = name_list.pop()
        
        except IndexError:
            i = name + " где-то гуляет"
            break
    return i         
            

name_list = ['Вася', 'Маша', 'Петя',  'Саша', 'Даша']
name = 'Валера'
print(find_person(name), 'нашёлся')


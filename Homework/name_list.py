name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

index = 0
name = name_list.pop(index)
while name != 'Валера':
    name = name_list.pop(index)
    index += 1
    
print(name, 'нашёлся')


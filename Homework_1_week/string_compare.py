# Написать функцию, которая принимает на вход 2 строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def string_compare(str1, str2):

    if str1 == str2:
        return 1
    elif len(str1) > len(str2): 
        return 2
    elif str2 == 'learn':
        return 3
    
        
str1 = input('Напишите что-нибудь: ')
str2 = input('Напишите что-нибудь ещё раз: ')

print(string_compare(str1, str2))
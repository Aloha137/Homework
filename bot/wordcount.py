# Добавить команду /wordcount котрая считает слова в присланной фразе. 
# Например на запрос /wordcount "Привет как дела" бот должен посчитать
# количество слов в кавычках и ответить: 3 слова 


def wordcount(phrase):
    if phrase:
        list_words = [word for word in phrase.split(' ') if word]
        return len(list_words)
    else:
        return "Введи что-нибудь по-братски,а ?!"
    

if __name__ == '__main__':
    print(wordcount(input("Введите фразу: "))) 
 
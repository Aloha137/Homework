# Добавить команду /wordcount котрая считает слова в присланной фразе. 
# Например на запрос /wordcount "Привет как дела" бот должен посчитать
# количество слов в кавычках и ответить: 3 слова 


def wordcount(args):
    if args:
#        args = [word for word in args.split(' ') if word]
        print(args)
        return "Фраза состоит из " + str(len(args)) + " слов/а"
    else:
        return "Введи что-нибудь по-братски,а ?!"
    

if __name__ == '__main__':
    print(wordcount(input("Введите фразу: "))) 
 
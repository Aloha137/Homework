#Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

scores_list = [
    {'school_class': '3a', 'scores': [3,5,4,1,2,4,4,5,5,2,2]},
    {'school_class': '3b', 'scores': [5,4,4,5,5,4,3,4,3,4,5,5,5,4]},
    {'school_class': '3c', 'scores': [3,2,2,1,2,3,4,3,2,2,2,2,3,]},
    {'school_class': '4a', 'scores': [3,4,4,3,5,3,3,3,4,2,3,4]},
    {'school_class': '4b', 'scores': [4,4,2,3,2,4,5,5,1,3,4,3]},
    {'school_class': '4c', 'scores': [3,2,3,5,4,3,2,1,2,5,5,4,4]},
    {'school_class': '5a', 'scores': [5,5,5,5,5,5,5,5,5,5]},
    {'school_class': '5b', 'scores': [4,5,2,3,1,4,5,3,4,5,5,2]},
    {'school_class': '5c', 'scores': [2,3,2,3,2,3,3,2,2,3,2,1,2,1]}
    ]
    # Вычислим средний балл по школе
    
def calc_av_school(scores_list):
    summ = 0
    index = 0
    for dictionary in scores_list:
        for score in dictionary['scores']:
            summ += score
            index += 1
    return round(summ/index)

def calc_av_class(scores_list):
    summ = 0
    index = 0
    for dictionary in scores_list:
        for score in dictionary['scores']:
            summ += score
            index += 1
        print(dictionary['school_class'], round(summ/index))

        
       
print(calc_av_school(scores_list))   # средний балл по школе
print(calc_av_class(scores_list))    # средний балл по классу
    
 

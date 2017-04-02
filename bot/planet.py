# добавьте в бота комманду /planet, которая будет принимать 
# на вход название планеты на английском. Затем при помощи 
# условного оператора if и ephem.constellation отвечать, 
# в каком созвездии сегодня находится планета.

import datetime
import ephem

date = datetime.datetime.now()

raw_planets_list = ephem._libastro.builtin_planets()
planets_list = {}



for _, type_, planet_name in raw_planets_list:
    if type_ != 'Planet':
        continue

    # let's create an object for all planets by their names from list
    a = getattr(ephem, planet_name)(date.strftime('%Y/%m/%d'))
    planets_list[planet_name.lower()] = ephem.constellation(a)[1]
        

def get_sign_by_planet(planet):
    try:
        sign = planets_list[planet.lower()]
    except KeyError:
        sign = 'В нашем списке нет такой планеты'
    return sign

if __name__ == '__main__':
    print(get_sign_by_planet(input('Введите планету на латинице: ')))
    
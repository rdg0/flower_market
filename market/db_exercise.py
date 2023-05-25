import django
import os

from random import choice
from typing import Dict, Type

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
django.setup()

from app.models import City, Person


# cities = ['Воронеж', 'Самара', 'Уфа', 'Томск', 'Ижевск', 'Таганрог']

# for city in cities:
#     City.objects.create(name=city)

# names = ['Игорь', 'Антон', 'Stepan', 'Petr', 'Gena', 'Боря', 'Egor', 'Stas', 'Прохор']

city_list = City.objects.all()

# for name in names:
#     city = choice(city_list)
#     Person.objects.create(city=city, name=name)

name_list = Person.objects.all()

# for city in city_list:
    # print(f'{city.pk} - {city.name}')


# print(Person.objects.filter(cities.name=='Краснодар').count())

# Сколько популяция города Краснодар
City.objects.get(name='Краснодар').cities.count()

q_1 = City.objects.get(name='Краснодар')

q = City.objects.filter(name='Краснодар')
print(City.objects.filter(name='Краснодар').query)
print(q[0])
print(q_1)
print(type(q_1))


# print(City.objects.filter(city.name=='Краснодар').count())
# print(qt_city.cities.count())

# for name in name_list:

#     print(f'{name.city.name} - {name.name}')
# print(len(name_list))

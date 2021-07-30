from js import my_json_w
from pk import my_pickle_w

my_favourite_group = {'name': 'Г.М.О.',
                    'tracks': ['Последний месяц осени', 'Шапито'],
                    'Albums': [{'name': 'Делать панк-рок','year': 2016},
                               {'name': 'Шапито','year': 2014}]
                     }
    
my_json_w(my_favourite_group)
print('--------------------------------------------------------')
my_pickle_w(my_favourite_group)
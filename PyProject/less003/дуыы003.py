#   1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#       Функция должна возвращать строку вида «Василий, 21 год(а),
#       проживает в городе Москва»

'''
def Datas(name='', age='', city=''):
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    city = input('Введите горо проживания: ')
    return F'{name}, {age} год(а), проживает в городе {city}'
print(Datas())
'''
#   С учетом разбора
'''
name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите горо проживания: ')

def Datas(name, age, city):
    return F'{name}, {age} год(а), проживает в городе {city}'
print(Datas(name,age,city))
'''

#   2: Создайте функцию, принимающую на вход 3 числа
#       и возвращающую наибольшее из них.
'''
def big_0(arg_0, arg_1, arg_2):
    return max(arg_0, arg_1, arg_2)
print(big_0(45,-15,10))

def big_1():
    args = []
    i = 0
    while i<3:
        a = int(input('Введите число:'))
        args.append(a)
        i += 1
    return max(args)
print(big_1())
'''
#   С учетом разбора
'''
def big_0(arg_0, arg_1, arg_2):
    rez = max([arg_0,arg_1,arg_2])
    return rez
print(big_0(45,-15,10))
'''

#   3: Давайте опишем пару сущностей player и enemy через словарь,
#   который будет иметь ключи и значения:
#       name - строка полученная от пользователя,
#       health = 100,
#       damage = 50.
#   Поэкспериментируйте с значениями урона и жизней по желанию.
#   Теперь надо создать функцию attack(person1, person2).
#       Примечание: имена аргументов можете указать свои.
#       Функция в качестве аргумента будет принимать атакующего и атакуемого.
#       В теле функция должна получить параметр damage атакующего
#       и отнять это количество от health атакуемого.
#       Функция должна сама работать со словарями и изменять их значения.
#   4: Давайте усложним предыдущее задание. Измените сущности,
#       добавив новый параметр - armor = 1.2 (величина брони персонажа)
#       Теперь надо добавить новую функцию, которая будет вычислять и возвращать
#       полученный урон по формуле damage / armor
#       Следовательно, у вас должно быть 2 функции:
#       1 Наносит урон. Это улучшенная версия функции из задачи 3.
#       2 Вычисляет урон по отношению к броне.
#       Примечание. Функция номер 2 используется внутри функции номер 1
#       для вычисления урона и вычитания его из здоровья персонажа.

'''
player = {'health': 100, 'damage': 40, 'arrmor': 1.2}
p_name = input('Введите имя Игрока')
player['name'] = p_name
enemy = {'name': 'zombie', 'health': 100, 'damage': 50, 'arrmor': 0.8}

def attack(strike, protected):
    nam_s = strike['name']
    print(nam_s)
    nam_p = protected['name']
    ene_h = protected['health']
    per_d = strike['damage']
    ene_a = protected['arrmor']
    dem_a = ene_h - per_d
    def dem(dem_a, ene_a):
        harm = dem_a/ene_a
        print(harm)
        return harm
    rez = dem(dem_a, ene_a)
    if rez <=0:
        print(F'Враг повержен {nam_p}')
        del protected
    else:
        protected['health'] = rez
        return protected

print(attack(player,enemy))
print(attack(enemy,player))
'''
#   С учетом разбора

p_name = input('Введите имя Игрока : ')
player = {'name': p_name,'health': 100, 'damage': 50, 'arrmor': 1.2}

e_name = input('Введите имя Игрока : ')
enemy = {'name': e_name, 'health': 50, 'damage': 30, 'arrmor': 1}

def uron(damage,arrmor):
    return damage / arrmor

def attack(strike, protected):
    damage = uron(strike['damage'], protected['arrmor'])
    protected['health'] -= damage

attack(player,enemy)
print(enemy)
attack(enemy,player)
print(player)


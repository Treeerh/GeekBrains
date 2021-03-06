#   Выполните практическое задание для отработки пройденного материала. Проверьте себя, посмотрев разбор задания в следующем уроке.
#   Проверка преподавателем в данном курсе не предусмотрена.

#   Практическое задание
#   1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#   Примечание. Списки создайте вручную, например так:

my_list_1 = [2,2,2,2,4,4,4,3,3,3,4,4,4,4,4,6,66,22,22,23,225,7,7,7,7,7,15,15,15]
print(my_list_1)
my_list_2 = [2, 7, 12, 33,17, 22, 15, 4, 46]
for my in my_list_2:
    for i in my_list_1:
        if my in my_list_1:
            my_list_1.remove(my)
print(my_list_1)

#   2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. Ваша задача — вывести дату в текстовом виде, например:
#   второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

while True:
    date_user = input('Введите дату в формате ДД.ММ.ГГГ')
    date_user = date_user.split('.')
    if 1 <= int(date_user[0]) <= 31 and 1<= int(date_user[1])<=12 and int(date_user[2])>=1000:
        break

date = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое',
        8: 'восьмое', 9: 'девятое', 10: 'десятое', 11: 'одинадцатое',
        12: 'двенадцатое', 13: 'тринадцатое', 14: 'четырнадцатое', 15: 'пятнадцатое',
        16: 'шеснадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое', 20: 'двацатое',
        21: 'двацать первое', 22: 'двацать второе', 23:'двацать тпетье', 24: 'двацать четвертое', 25: 'двацать пятое',
        26: 'двацать шестое', 27: 'двацать седьмое', 28: 'двацать восьмое', 29: 'двацать девятое',
        30: 'тридцатое', 31: 'тридцать первое'}
month = {1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: 'Июля', 8: 'Августа', 9: 'Сентября',
         10: 'Октября', 11: 'Ноября', 12: 'Декабря'}

print (F'{date[int(date_user[0])]} {month[int(date_user[1])]} {date_user[2]} года')


#   3: Дан список заполненный произвольными целыми числами.
#   Получите новый список, элементами которого будут только уникальные элементы исходного.
#   Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []
count={}

for i in my_list_1:
    count[i]=my_list_1.count(i)
print(count)
for key, val in count.items():
    if val==1:
        my_list_2.append(key)

print(my_list_2)

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_1.sort()

#   Второй вариант

my_list_2 = list(set(my_list_1))
my_list_2.sort()

tree = {}

for my in my_list_2:
    count =0
    for i in my_list_1:
        if my ==i:
            count +=1
    tree[my] = count
del count
my_list_1.clear()
for key, val in tree.items():
    if val == 1:
        my_list_1.append(key)

print(my_list_1)
del my_list_1
del my_list_2
del tree
#В этом случае ответ будет:
#[5, 8]
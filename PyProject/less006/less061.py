#   ГЕНЕРАТОРЫ

nums = [1,2,3,4,-5,-7,-8,9]
# Класический
rez = []
for number in nums:
    if number > 0:
        rez.append(number)
print(rez)

#   Через filters
rez = []
rez = filter(lambda number: number>0, nums)
print(list(rez))

#   Через ГЕНЕРАТОР
rez = [number for number in nums if number > 0]
print(rez)

#   ГЕНЕРАТОР СЛОВАРЯ
#   Класический
pairs = [(1, 'a'),(2, 'b'),(3, 'c')]
print(pairs)
print(type(pairs))
rez = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    rez[key] = val
print(rez)
print(type(rez))

#   Через ГЕНЕРАТОР
rez = {pair[0]: pair[1] for pair in pairs}
print(rez)
#   ПРИМЕРЫ
#   1
import random
nums = [random.randint(1,100) for i in range(10)]
print(nums)
#   2
nums = [1,2,3,4,5,6,-8]

rez = [i**2 for i in nums]
print(rez)
#   3
names = ['Саша','Александр','Андрей','Михаил','Антон','Глеб','Матвей']
rez = [name for name in names if name.startswith('А')]
print(rez)




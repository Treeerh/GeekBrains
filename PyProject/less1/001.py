#   1: Запросите от пользователя число, сохраните в переменную, прибавьте к
#       числу 2 и выведите результат на экран. Если возникла ошибка, прочитайте
#       ее, вспомните урок и постарайтесь устранить ошибку.

figure = int(input('Введите число: '))
print('Ваше число', figure,'увеличенное на 2:', figure+2)

#   2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
#       После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
#       Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
#       Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

figure = None
while True:
    figure = int(input('Введите число: '))
    if figure > 0 and figure < 10:
        print('Число в квадрате = ', figure**2)
        break
    else:
        print('Введите число от 0 до 10')
#   3: Создайте программу “Медицинская анкета”, где вы запросите у
#       пользователя следующие данные: имя, фамилия, возраст и вес.

name = input('Введите ваше имя :')
family = input('Введите вашу Фамилию :')
age = int(input('Введите ваш возраст :'))
heft = int(input('Введите ваш вес :'))

if age < 30 and heft >= 50 and heft <=120:
    print('Пациент', name, family, 'в возрасте', age,'в хорошем состоянии')
elif age > 30 and heft < 50 or heft > 120:
    print('Пациенту', name, family, 'в возрасте', age, 'требуется занятся собой')
elif age > 40 and heft < 50 or heft > 120:
    print('Пациенту', name, family, 'в возрасте', age, 'требуется врачебный осмотр')
else:
    print('Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.')

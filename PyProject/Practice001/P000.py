import random

num = random.randint(0,100)
print(num)

us_num = None
while num != us_num:
    us_num = (input('Введите число : ')
    if num < us_num:
        print(">")
    else:
        print("<")
print('WIN')


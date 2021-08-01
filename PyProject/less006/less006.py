#   Тернальные операторы
is_has_name = False

name = 'Max' if is_has_name else 'Hello'
print(name)

is_one = True
number = 1 if is_one else 2
print(number)

is_rus = False
print('Привет' if is_rus else 'Hello')

#1 От IF  к ТЕРНАЛЬНОМУ оператору

word = 'Слово'
rez = []
for i in range(len(word)):
    if i%2 != 0:
        let = word[i].lower()
    else:
        let = word[i].upper()
    rez.append(let)
rez = ''.join(rez)
print(rez)

rez = []
for i in range(len(word)):
    #let = word[i].lower() if i%2 !=0 else word[i].upper()   #или
    let = word[i]
    let = let.lower() if i % 2 != 0 else let.upper()

    rez.append(let)

print(rez)
print(type(rez))
rez = ''.join(rez)


print(rez)
print(type(rez))

password =input('Введите пароль: ')
print('go' if password == '1234' else 'exit')




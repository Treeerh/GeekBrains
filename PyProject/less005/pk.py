import pickle as pk


def my_pickle_w(my_grup):
    with open('dump.pickle', 'wb') as fp:
        pk.dump(my_grup, fp)
        print('PICKLE Записан в файл')

def my_pickle_r():
    with open('dump.pickle', 'rb') as fp:
        my_pick = pk.load(fp)
        print('PICKLE Прочитан из файла')
        print (my_pick)
        print(type(my_pick))
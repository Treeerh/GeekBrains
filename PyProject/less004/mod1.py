#import os
from os import getcwd,path,listdir,mkdir,rmdir
#path = os.getcwd()  # Для проверки модуля

def create_dir(way):
    for i in range(1,10):
        new_path = path.join(way, 'dir_{}'.format(i))
        mkdir(new_path)
        print('Создано',new_path)

#
def delete_dir(way):
    pas = listdir(way)
    for i in pas:
        fol= i[:4]
        if i.find('dir_') == 0:
            print('Удалено',path.join(way,i))
            rmdir(path.join(way,i))

''' Проверка в модуле
create_dir(path)   # Создание папок
delete_dir(path)   # Удаление папок 
'''



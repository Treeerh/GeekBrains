import json as js


def my_json_w(my_grup):
    with open('dump.json', 'w', encoding='utf-8') as fp:
        js.dump(my_grup, fp)
        print('JSON Записан в файл')

def my_json_r():
    with open('dump.json', 'rb') as fp:
        my_json = js.load(fp)
        print('JSON Прочитан из файла ')
        print(my_json)
        print(type(my_json))

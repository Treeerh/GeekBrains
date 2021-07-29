#import random

from random import choice

def rend_list(my_list):
    if len(my_list) == 0:
        return None
    else:
        return choice(my_list)

my_list = [1,2,3,4,5,6,7,8,9]
my_zero = []
if __name__ == '__main__':
    print(rend_list([]))
    print(rend_list(my_list))
    print(rend_list(my_zero))
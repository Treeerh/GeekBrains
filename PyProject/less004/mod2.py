#import random

from random import choice

def rend_list(my_list):
    if len(my_list) == 0:
        return None
    else:
        return choice(my_list)


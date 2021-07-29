#import mod1
#import mod2

from mod1 import create_dir,delete_dir,getcwd
from mod2 import rend_list


path = getcwd()

create_dir(path)

delete_dir(path)

my_zero = []
my_list = [0,1,2,3,4,5,6,7,8,9]

print(rend_list(my_zero))
print(rend_list(my_list))
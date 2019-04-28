import mod1
#import mod2
import sys
from pprint import pprint

def print_dict(d):
    for key, val in d.items():
        print(f'{key}:{val}')

#pprint(sys.path)

#print('dir=', dir())

mod1.func1()

#mod1.func2()

#mod2.func1()

#print(f'dir(mod1)={dir(mod1)}')

#print(f'in prog1: l1={mod1.l1}')


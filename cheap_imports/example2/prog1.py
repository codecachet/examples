from mod1 import func1

from pack1.mod1 import x
from pack1.mod2 import x as y

#import pack1.mod2

#from pack1 import *
#x = mod1.x
#y = mod2.x

func1()

print(f'the value of pack1.mod1.x={x}')

print(f'the value of pack1.mod2.x={y}')

#print(f'file={pack1.mod2.__file__}')
#print(f'pac1.mod2.x={pack1.mod2.x}')
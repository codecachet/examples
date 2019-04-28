import mod1
from mod1 import var1 as var
#from mod1 import *
from mod2 import func1
#import mod1
#from mod1 import l1


print(f'dir(mod1) = {dir(mod1)}')

print(f'called from prog2, mod1.l1 = {mod1.l1}')
print(f'called from prog2, mod1.var1 = {mod1.var1}')

print(f'this be var in prog1 = {var}')
#print(f'called from porg2, l1={l1}')

func1()
"""
if xx

if xx
else

if xx
elif

a = b if x

or
and
not

"""

def sound(a):

    if a == 'lion':
        s = 'roar'
    elif a == 'cat':
        s = 'meow'
    elif a == 'dog':
        s = 'bowow'
    else:
        s = 'grrr'
    return s
    
def disturb(a):
    s = f'The {a} will go {sound(a)} if you disturb it'
    return s

def doit(a):
    mys = disturb(a)
    print(mys)
    
def doall():
    doit('lion')
    doit('dog')
    doit('orangotan')



doall()
    

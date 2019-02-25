# short circuit
def f1():
    print('f1 here')
    return True
    
def f2():
    print('f2 here')
    return True

def f3():
    print('f3 here')
    return True

def ourtest():
    if f1() and f2() and f3():
        print('all true')

ourtest()

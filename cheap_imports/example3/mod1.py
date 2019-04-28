def func1():
    print('this is func1 in mod1')

def func2():
    print('this is func2 in mod1')

def test():
    print('testing mod1...')
    func1()
    func2()

#print(f'__name__ in mod1 ={__name__}')

test()
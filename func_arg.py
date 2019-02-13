# example of calling a function with a function as an arg

def func1(animal):
    s = f'My favorite animal is the {animal}'
    return s

def func2(animal):
    s = f'I really like my {animal}, as it is the greatest'
    return s

def best_friend(f):
    return f('dog')

def test():
    s = best_friend(func1)
    print(f's={s}')
    s = best_friend(func2)
    print(f's={s}')


test()


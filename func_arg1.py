# example of a function taking a function as an argument
def func1(string, f):
    s = string + " a good time"
    s1 = f(s)
    return s1

def func2(string):
    s = string.title()
    return s

def func3(string):
    s = string.upper()
    return s

def test():
    s = "what to do to have"
    
    s1 = func1(s, func2)
    print(f's1={s1}')

    s1 = func1(s, func3)
    print(f's1={s1}')

test()
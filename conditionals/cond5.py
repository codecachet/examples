def f1(y):
    a = 5
    b = 10
    
    c = a if y == 5 else b
    
    print(f'c={c}')
    
def doit():
    y = 7
    f1(y)

doit()

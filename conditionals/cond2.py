def get_num():
    print('enter number:')
    n = input()
    n = int(n)
    return n

def analyze(n):
    if n == 0:
        print('really bad')
    elif n == 1:
        print('bad')
    elif n >= 2 and n <= 3:
        print('ok')
    elif n == 4:
        print('pretty good')
    elif n == 5:
        print('stellar')
    elif n >= 10:
        return
    else:
        print('bad number,try again')

def doit():
    n = 0
    while n < 10:
        n = get_num()
        analyze(n)
    print('done')

doit()



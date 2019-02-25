def loop1(max):
    n = 0
    x = 0
    while n <= max:
        x += n
        n += 1
    return x

def addthem():
    max = 6
    n = loop1(max)
    print(f'result={n}')

addthem()

from random import randint

def shuffle(a):
    """
    produce a new array
    """
    n = len(a)
    res = []

    for i in range(0, n):
        print(f'i={i}')
        rint = randint(0, n - i - 1)
        print(f'rint={rint}')
        res.append(a[rint])
        del a[rint]
    return res

if __name__ == "__main__":
    #a = [0, 1, 2, 3, 4]
    a = [0, 1]
    b = shuffle(a)
    print(f'b={b}')
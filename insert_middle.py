# insert substring in middle of odd-length string
def insert_middle(string, substring):
    lstring = len(string)
    middle = lstring // 2
    print(f'middle={middle}')
    first = string[:middle]
    second = string[middle + 1]
    print(f'first={first}')
    print(f'second={second}')

    r = f'{string[:middle]}{substring}{string[middle + 1:]}'
    return r


def test():
    string = 'abcde'
    substring = 'dog'
    r = insert_middle(string, substring)
    print(f'r={r}')

test()
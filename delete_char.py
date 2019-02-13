# delete n'th character from string

def delete_n(s, n):
    # assume n < len(s)

    r = s[:n] + s[n+1:]

    return r

def test():
    s = '0123456'
    r = delete_n(s, 3)
    print(f'r={r}')

test()
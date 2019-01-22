
def remove_dups(a):
    """produce new array"""
    res = []
    dups = []

    for i,val in enumerate(a):
        if val in dups:
            continue
        if val not in a[i:]:
            res.append(val)
        else:
            res.append(val)
            dups.append(val)
    return res


if __name__ == "__main__":
    a = [3]*3
    print(f'a={a}')
    b = remove_dups(a)
    print(f'b={b}')

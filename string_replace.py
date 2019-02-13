# write a string replace, using find (and assume that the subsr exists)

def string_replace(string, search, rep):
    f = string.find(search)
    # ASSUME f >= 0 !!!!
    #s1 = string[:f] + rep + string[f + len(search):]
    s1 = f'{string[:f]}{rep}{string[f + len(search):]}'
    return s1

def test():
    s = "Now is the time to learn PHP and other stuff"
    r = string_replace(s, 'PHP', 'Python')
    print(f'r = {r}')

test()
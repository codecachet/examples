# return count of substrings, ignoring case
def n_substrings(string, substring):
    string = string.lower()
    substring = substring.lower()
    count = string.count(substring)
    return count

def test():
    s1 = 'The Cat and the Hat and another hat and more HAts'
    n = n_substrings(s1, 'CAt')
    print(f'cat n={n}')

    n = n_substrings(s1,'HAT')
    print(f'hat n={n}')

test()
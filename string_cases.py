# create upper, lower, title case of string

def string_cases(string):
    s1 = string.upper()
    s2 = string.lower()
    s3 = string.title()

    return s1, s2, s3

def test():
    s = 'Hello all, how do you do?'
    s1, s2, s3 = string_cases(s)

    print(f's1={s1}')
    print(f's2={s2}')
    print(f's3={s3}')

test()
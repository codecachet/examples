# add html tag around word
def html_tag(tag, word):
    s = f'<{tag}>{word}</{tag}>'
    return s


def test():
    res = html_tag('b', 'dog')
    print(f'res={res}')
    html_tag('div', 'cat')
    print(f'res={res}')

test()

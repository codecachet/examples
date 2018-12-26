import hashlib

def hashit(str):
    hstr = hashlib.md5(str)
    print('hstr=', hstr.hexdigest())
    
    return hstr.hexdigest()
    
def number2base(n, b):
    print('n=', n)
    if n == 0:
       return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    #return digits[::-1]
    print( ' digits=', digits[::-1])
    return digits[::-1]

def digits2str(chars, digits):
    charlist = [chars[digit] for digit in digits]
    str = "".join(charlist)
    return str

def crack1(hashstr):
    #chars = "@abcdefghijklmnopqrstuvwxyz"
    # first char needs to be one which is never in the password
    chars = '\0abcd'
    max_char = 2
    
    base = len(chars)
    max = base ** max_char
    for n in range(max):
        digits = number2base(n, base)
        if 0 in digits:
            continue
        str = digits2str(chars, digits)
        print("str=", str)
        hash1 = hashit(bytearray(str.encode()))
        if hash1 == hashstr:
            print("Cracked! password is ", str)
            return
    else:
        print('cannot crack!')

def test():
    for i in range(20):
        d = number2base(i, 5)
        print("i=", i, " d=", d)

def doit():
    h = hashit(b'da')
    crack1(h)

if __name__ == "__main__":
    doit()

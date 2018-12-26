import hashlib
import random

def hashit(str):
    hstr = hashlib.md5(str)
    print('hstr=', hstr.hexdigest())
    
    return hstr.hexdigest()

def randstr(nchars, charlist):
    the_list = [ random.choice(charlist) for i in range(nchars) ]
    print("thelist=", the_list)
    str = ''.join(the_list)
    return str
    
def next_str(curlist, nchars, charlist):
    # do for one for test
    clen = len(charlist)
    
    if curlist[0] >= clen:
        curlist[0] = 0 
    else:
        curlist[0] += 1
    
    mycharlist = []
    
    for i in curlist:
        if i != -1:
            mycharlist.append(charlist[curlist[i]])
    return ''.join(mycharlist)

def crack1(hstr):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    
    max_nchar = 5
    
    cand = [-1 for i in range(max_nchar)]
    print("cand=", cand)
    
    for i in range(max_nchar):
        print("i=",i)
        rangen = len(chars)*(i + 1)
        print("rangen=", rangen)
        for j in range(rangen):
            #str1 = randstr(i + 1, chars)
            str1 = next_str(cand, i + 1, chars)
            hash1 = hashit(bytearray(str1.encode()))
            if hash1 == hstr:
                print("Cracked! password is ", str1)
                return
    print("no answer")      
        
def doit():
    h = hashit(b'd')
    crack1(h)

if __name__ == "__main__":
    doit()



















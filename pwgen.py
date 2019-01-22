import random

#random.seed(1)

def get_random_char(chars):
    lenchars = len(chars)
    r = random.randint(0, lenchars - 1)
    return chars[r]

def pw1(nchars):
        
    mychars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    newpass = ''
    for _ in range(nchars):
        c = get_random_char(mychars)
        newpass = newpass + c

    return newpass
	
def create_passwords():
    for i in range(10):
        pw = pw1(25)
        print(f'i={i}, password= {pw}')

if __name__ == '__main__':
    create_passwords()

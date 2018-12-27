import random

def get_random_char(chars):
    lenchars = len(chars)
    r = random.randint(0, lenchars - 1)
    return chars[r]

def pw1():
    newpass = ""
    mychars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+"
	
    for i in [0, 1, 2, 3, 4]:
        c = get_random_char(mychars)
        newpass = newpass + c

    return newpass
	
def create_passwords():
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        pw = pw1()
        print(i, " : ", "password = ", pw)

create_passwords()

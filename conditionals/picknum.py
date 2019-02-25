import random

def getnum():
    n = random.randint(0, 10)
    return n

def doit():
    num = getnum()
    count = 0
    while(True):
        count += 1
        guess = int(input('give guess: '))
        if guess == num:
            print(f'you guessed it,num={num} after {count} guesses')
            break
    print('done')
doit()

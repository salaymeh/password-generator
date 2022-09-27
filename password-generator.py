import random 

import sys


def passwordGenertor():
    lowerchars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperchars=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    specialchars=['?','>','!','<','"',':',';','{','[',']','}','|','\\','~','@','#','$','%','^','&','*','*','(',')','-','+','-','=']
    numbers=['1','2','3','4','5','6','7','8','9','0']

    randomLetters=random.choice(lowerchars)+random.choice(upperchars)+random.choice(lowerchars)+random.choice(upperchars)
    randomNumbers=random.choice(numbers)+random.choice(numbers)

    password=random.choice(lowerchars)+random.choice(upperchars)+random.choice(specialchars)+random.choice(numbers)
    password=randomLetters+password+randomNumbers

    return password

def numberOfPasswords(num):
    i=0
    while i < num:
        print("password "+str(i+1)+": "+passwordGenertor())
        i=i+1



def main():

    numberOfPasswords(int(sys.argv[1]))

if __name__ == "__main__":
    main()
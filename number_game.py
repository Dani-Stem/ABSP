#the number game? wanna test ur psychic abilities?? lets see if u can guess what number this program is thinking of...

import sys
import random

num = random.randint(1,10)
guess = int(input("Hello, lets play a game, i am thinking of a number 1 through 10.. what is it? "))
tries = int()

while guess!=num and tries < 5:
    try:
        if guess < num:
            guess = int(input('wrong, try guessing higher: '))
        elif guess > num:
            guess = int(input('wrong try guessing lower: '))
        tries +=1
    except ValueError:
        print('plz enter a number.')

if tries == 5:
    print('u ran out of tries, oops. the number was ' + str(num) + '.')
else:
    print('niceeee')


    
    

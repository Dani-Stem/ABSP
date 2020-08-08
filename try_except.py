#wow theres alot of people here, how many slices does each person get?? a program to help you

try:
    
    print('How many people are eating the pizza? ')
    ppl = input()
    ppl = int(ppl)

    print('How many slices do u have? ')
    slices = input()
    slices = int(slices)

    #the answer 
    ans =  int(ppl) / int(slices)
    print('each person can have ' + str(ans) + ' many slices.')



except ValueError:
    print('plz enter a number')

except ZeroDivisionError:
    print('please enter a number of slices greater than 0')


#this program wants to know what you ate for breakfast

bfast = input("So tell me, did you eat breakfast this morning? ").lower()

if bfast == 'y':
    food = input('Prada ya! what did you eat?').lower()
    if food[0] in ['a','s','d','f','g','h','j','k','l']:
            print('Yum, jelious. goodbye')
    elif food[0] in ['q','w','e','r','t','y','u']:
        print('there alot of calories in that')
    elif food[0] in ['z']:
        print('u ate zucchini??')
    elif food[0] in ['x','c','v']:
        print('zoomin in the foreign, got the engine roaring')
    else:
        print('Wow you ate a lot! Munchies???').lower()
elif bfast == 'n': 
    print('Plz dont talk to me unless u have eaten breakfast. goodbye')
else:
    print('i dont understand ur answer..')



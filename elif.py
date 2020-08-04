#this program wants to know what you ate for breakfast

bfast = input("So tell me, did you eat breakfast this morning? ").lower()

if bfast == 'y':
    food = input('Prada ya! what did you eat?').lower()
    if food == ['a','s','d','f','g','h','j','k','l']:
            print('Yum, jelious. goodbye')
    else:
        print('fsfaef')
elif bfast == 'n'or bfast == 'N': 
    print('Plz dont talk to me unless u have eaten breakfast. goodbye')
else:
    print('i dont understand ur answer..')



for numbers in range(1, 101):

    if (numbers % 3 == 0 and numbers % 5 != 0):

        print('pie')

    elif (numbers % 5 == 0 and numbers % 3 != 0):

        print('thong')

    elif (numbers % 3 == 0 and numbers % 5 ==0):

        print('piethong')

    else:
        
        print(numbers)
        
    

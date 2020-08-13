#this program lets the user pick recipes to add to their grocery list


glist = {}
recipes = {
    'chxTaco':['chx', 'tortillas', 'chz'],
    'blueberryMuffins':['blueberries', 'flour', 'sugar'],
    'quesadilla':['salt', 'tortillas', 'chz'],
    'cake':['flour', 'egg', 'sugar']
}

while (input('would up like to add a recipes to ur grocery list? y/n: ').lower() == 'y'):

    print(' ')
    print('Hello, here are the recipes for today: ')
    print(' ')
    print('Recipe #1 Chicken Tacos: ')
    print(','.join(recipes['chxTaco']))
    print(' ')
    print('Recipe #2 Blueberry Muffins: ')
    print(','.join(recipes['blueberryMuffins']))
    print(' ')
    print('Recipe #3 Quesadilla: ')
    print(','.join(recipes['quesadilla']))
    print(' ')
    print('Recipe #4 Cake: ')
    print(','.join(recipes['cake']))
    print(' ')

    path = int(input('which recipe # do u want to add to ur grocery list?: '))
    if path == 1:
        print('adding Chicken Tacos to ur shopping list...')

        for i in recipes['chxTaco']:
            if (i in glist):
                glist[i] += 1
            else: 
                glist[i] = 1

        print('Ur currrent grocery list: ')
        print(glist)

    elif path == 2:
        print('adding Blueberry Muffins to ur shopping list...')

        for i in recipes['blueberryMuffins']:
            if (i in glist):
                glist[i] += 1
            else: 
                glist[i] = 1

        print('Ur currrent grocery list: ')
        print(glist)

    elif path == 3:
        print('adding Quesadilla to ur shopping list...')

        for i in recipes['quesadilla']:
            if (i in glist):
                glist[i] += 1
            else: 
                glist[i] = 1

        print('Ur currrent grocery list: ')
        print(glist)

    elif path == 4:
        print('adding Cake to ur shopping list...')

        for i in recipes['cake']:
            if (i in glist):
                glist[i] += 1
            else: 
                glist[i] = 1

        print('Ur currrent grocery list: ')
        print(glist)

print('bye')

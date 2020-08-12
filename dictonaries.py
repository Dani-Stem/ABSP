#this program lets the user pick recipes to add to their grocery list

glist = {}
recipes = {
    'chxTaco':['chx', 'tortillas', 'chz'],
    'blueberryMuffins':['blueberries', 'flour', 'sugar'],
    'quesadilla':['salt', 'tortillas', 'chz'],
    'cake':['flour', 'egg', 'sugar']
}

print('Hello, here are the recipes for today: ')

print('Recipe #1 Chicken Tacos: ')
print(recipes['chxTaco'])

path = input('would u like to add this recipe to ur grocery list? y/n: ').lower()

if (path == 'y'):
    print('adding Chicken Tacos to ur shopping list...')

    for i in recipes['chxTaco']:
        if (i in glist):
            glist[i] += 1
        else: 
            glist[i] = 1
    print('Ur currrent grocery list: ')
    print(glist)
    path1 = input('would u like to add another recipe? y/n: ').lower()
    if path1 == 'y':
        print('returning to recipes...')
        
    else:
        print('Ur currrent grocery list: ')
        print(glist)
        quit()
    
print('Recipe #2 Blueberry Muffins: ')
print(recipes['blueberryMuffins'])

path = input('would u like to add this recipe to ur grocery list? y/n: ').lower()

if (path == 'y'):
    print('adding Blueberry Muffins to ur shopping list...')

    for i in recipes['blueberryMuffins']:
        if (i in glist):
            glist[i] += 1
        else: 
            glist[i] = 1
    print('Ur currrent grocery list: ')
    print(glist)
    path1 = input('would u like to add another recipe? y/n: ').lower()
    if path1 == 'y':
        print('returning to recipes...')
        
    else:
        print('Ur currrent grocery list: ')
        print(glist)
        quit()

print('Recipe #3 Quesadilla: ')
print(recipes['quesadilla'])

path = input('would u like to add this recipe to ur grocery list? y/n: ').lower()

if (path == 'y'):
    print('adding Quesadilla to ur shopping list...')

    for i in recipes['quesadilla']:
        if (i in glist):
            glist[i] += 1
        else: 
            glist[i] = 1
    print('Ur currrent grocery list: ')
    print(glist)
    path1 = input('would u like to add another recipe? y/n: ').lower()
    if path1 == 'y':
        print('returning to recipes...')
        
    else:
        print('Ur currrent grocery list: ')
        print(glist)
        quit()

    
print('Recipe #3 Cake: ')
print(recipes['cake'])

path = input('would u like to add this recipe to ur grocery list? y/n: ').lower()

if (path == 'y'):
    print('adding Cake to ur shopping list...')

    for i in recipes['cake']:
        if (i in glist):
            glist[i] += 1
        else: 
            glist[i] = 1
print('Ur currrent grocery list: ')
print(glist)



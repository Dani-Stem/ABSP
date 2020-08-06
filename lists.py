 #name smasher 


fnamelist = []
lnamelist = []

done = ''

while done != 'n':
    fname = input('plz enter a first name: ')
    lname = input('plz enter a last name: ')
    fsmashed = fname[:3]
    lsmashed = lname[:3]


    fnamelist.append(fsmashed)
    lnamelist.append(lsmashed)

    done = input('would u like to add another name? y/n: ').lower()

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

fname = concatenate_list_data(fnamelist)
lname = concatenate_list_data(lnamelist)

print(fname)
print(lname)

"""
x = input("entré un nombre")
if x.isdigit() :
    o = input("entré un opérateur")
    if '*''/''+''-' in o :
        y = input("entré un nombre")
        if y.isdigit() :
            if '*' in o:
                p=x*y
            if '/' in o:
                p = x / y
            if '+' in o:
                p = x + y
            if '-' in o:
                p = x - y
        else

    else :

x = int(input('inserer un nombre'))

for iterateur in range(x+1):
    print("5 x ",iterateur," = ",5*iterateur)"""

x = int(input('inserer un nombre'))

for i in range(x+1):

    print(str(i)[::-1])


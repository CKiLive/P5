

c = input("chaine")
res = True

for i in range(0,len(c)//2):
    if c[i]!=c[i+1]:
        res = False

if res :
    print( "oui")
else :
    print ("non")
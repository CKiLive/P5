from random import randint

n = randint(0, 100)
t = 0
e = 0
while t == 0 and e < 10:
    e = e + 1
    u = int(input("choisisser un nombre "))
    if n > u:
        print("le nombre à trouver est plus grand")
    else:
        if n < u:
            print("le nombre à trouver est plus petit")
        else:
            if n == u:
                print("gagnier en", e, "essais")
                t = 1

            else:
                print("erreur")
if t == 0:
    print("tu à rater", e, "fois tu à perdu ")

n = float(input("quel est votre moyenne générale au bac ?"))

if n>=20:
    print ("exelence")
else :
    if n >= 16:
        print("très bien")
    else:
        if n >= 14:
            print("bien")

        else:
            if n >= 12:
                print("assez bien")

            else:
                if n>=10:
                    print ("obtenue")
                else :
                    print ("rater")
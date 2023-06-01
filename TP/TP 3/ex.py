n = int(input("valeur de n"))
t = "est divisable par"
tt = "n'st pas divisable par"

if n // 2 == n / 2:
    print(n, t, "2")
else:
    print(n, tt, "2")

if int(n / 3) == n / 3:
    print(n, t, "3")
else:
    print(n, tt, "3")

if int(n / 5) == n / 5:
    print(n, t, "5")
else:
    print(n, tt, "5")

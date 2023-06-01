n = int (input("valeur de n"))
s = 0
for i in range (-10,n):
    s = i + 5*i + i*i + s
print(s)
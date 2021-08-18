d = "*"

k = 1
v = int(input("Number: "))
for i in range (v):
    for w in range (v - i):
        print(" ",end = "")
    for m in range (k):
        print(d ,end = "")
    k += 2
    print("")
o = k - 4
z = o
for n in range ( v - 1 ):
    for p in range ( 2 + n  ):
        print(" ", end = "")
    for q in range (z):
        print(d,end = "")
    z =  z - 2
    print("")




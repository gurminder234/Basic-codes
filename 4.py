n = int(input(" number : "))
if n == 2:
    print("Prime no.")

for i in range(2 , n-1,1):
    if ((n % i) == 0):
        print("Not a prime no.")
    else:
        print("Prime no.")
    break

isPrime = True
for k in range (2,n-1,1):
    if ((n % k) == 0):
        isPrime = False

if (isPrime):
    print("Prime no.")
else:
    print("Not a prime no.")

n = int(input("= "))

for q in range (2,int((n/2 +1)),1):

    if ((n % q) == 0):
      isPrime = False


if (isPrime):
    print("Prime no.")
else:
    print("Not a prime no.")
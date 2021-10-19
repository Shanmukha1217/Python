N = int(input('Enter the number: '))
factors = 0


for i in range(1,N+1):
    if N % i == 0:
        factors +=1

if factors == 2:
    print(f"{N} is a prime number")
else:
    print(f'{N} is not prime number')
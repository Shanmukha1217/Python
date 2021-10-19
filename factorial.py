#Program to find the factorial of a number

num = int(input('Enter the number: '))
fact = int(1)

for n in range(1, num+1):
    fact = fact * n

print(fact)


# program to print all the factors of a factorial number

num = int(input('Enter the numbe: '))
sum = int()
for i in range(1,num+1):
    if num % i == 0:
        sum += i
        print(i)
print(f'sum of all factors of a number {num} is {sum}')


# # Program to find whether the given number is perfect number or not

N = int(input('Enter the number: '))
s = 0
for i in range(1,N):
    if N % i == 0:
        s += i
if s == N:
    print(f'{N} is a perfect number')
else:
    print(f'{N} is not perfect number')



# program to find number of factors of a given number
N = int(input('Enter the number: '))
factors = 0
for i in range(1,N+1):
    if N % i == 0:
        factors +=1
print(factors)
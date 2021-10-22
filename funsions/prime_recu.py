def prime_num(i,num):
    if num == i:
        return 0
    else:
        if(num % i == 0):
            return 1
        else:
            return prime_num(i+1,num)


start = int(input('Enter the start bound: '))
end = int(input("Enter your end bound: "))

for i in range(start, end - 1):
    if(prime_num(2,i) == 0):
        print(i)
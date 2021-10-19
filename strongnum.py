num = int(input('enter a number: '))
temp = num
strong= int()

while temp:
    last_digit = temp % 10
    fact = 1
    for n in range(1,last_digit + 1):
        fact = fact * n
    temp //= 10
    strong += fact

if strong == num:
    print(f'{num} is a strong number')
else:
    print(f'{num} is not a strong number')




num = int(input('Enter a num: '))
temp = num
res = int()
while temp:
    last_digit = temp % 10
    res = (res*10) + last_digit
    temp //= 10

print(f'reverse of a given {num} is {res}')

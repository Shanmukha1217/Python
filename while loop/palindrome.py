num = int(input('Enter a num: '))
temp = num
res = int()
while temp:
    last_digit = temp % 10
    res = (res*10) + last_digit
    temp //= 10

if num == res:
    print(f'{res} is same as {num} it is palindrome')
else:
    print(f'{res} is not same a {num} so its not palindrome')
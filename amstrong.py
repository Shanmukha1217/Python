num = int(input('enter a number: '))
temp = num
count = 0
res = int()

while temp:
    temp //= 10
    count += 1

temp = num

while temp:
    last_digit = temp % 10
    res += (last_digit ** count)
    temp //= 10

if num == res:
    print(f'{num} = {res} its an amstong number')
else:
    print(f'{num} != {res} its not an amstong number')





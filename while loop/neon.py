#### Neon number


# num = int(input('Enter a num: '))

square = num * num
temp = square
res=int()

while temp:
    last_digit = temp % 10
    res += last_digit
    temp //= 10

# if res == num:
#     print(f'number = {num} and result =  {res} are same so its Neon number ')
# else:
#     print(f'number = {num} and result = {res} are not equal so its not a neon number')


#### Automorphic number

num = int(input('ent: '))
square = num ** 2
temp = num
boolean = True

while temp:
    if temp % 10 != square % 10:
        boolean = False
        break
    temp //= 10
    square //=10

if boolean == True:
    print(f'{num} is automorphic')
else:
    print(f'{num} is not automorphic')
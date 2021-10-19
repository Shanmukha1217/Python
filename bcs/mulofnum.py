# code to find whether the given number is multiple of another number or not

num1  = int(input('Enter the number to be checked: '))
num2 = int(input('Enter the number: '))

if num2 % num1 == 0:
    print('{} ia a multiple of {}'.format(num1,num2))
else:
    print('{} ia not multiple of {}'.format(num1,num2))

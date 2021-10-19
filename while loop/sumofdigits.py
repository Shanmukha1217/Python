# Progran to find sum of all the digits of a given number

# num = input('enter a number')
# sum = 0

# for a in str(num):
#     sum += int(a)
# print(sum)

# ////////

num = int(input('Enter an integer: '))
temp = num
res =int()

while temp:
    last_digit = temp % 10
    res += last_digit 
    temp //= 10
    
print(f'Sum of all the digits of {num} is {res}')

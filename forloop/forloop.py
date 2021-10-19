# for var in range(1,11,1):
#     print(var)
   


# for num in range(0,101):
#     # print(num)
#     if num % 2 == 0:
#         print(num)

# for a in range(250,-251,-1):
#     print(a) 


# Program to find sum of all multiples on till m

# n = int(input('Enter the number n: '))
# m = int(input("Enter the number m: "))
# final_result= int()

# for num in range(1, m + 1):
#     res = num * n
#     final_result += res 
#     print(f'{n} * {num} = {res}')

# print(f'sum of multiples of {n} till {m} is {final_result}')


# Program to print all the perfect square till 500

sum = int()
for num in range(1,51):
    square = num **2 
    if square <= 50 and square % num == 0:
        sum += square
        print (square)
    else:
        break
print(f'sum of all the perfect squares till 50 is {sum}')



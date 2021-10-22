# def fact():
#     num = int(input('enter a num: '))
#     res = int(1)
#     for i in range(num,1 ,-1):
#         res *= i
#     print(f'The factorial of a number{num} is {res}')

# fact()

# def factorial(num):
#     fact = 1
#     for n in range(num,1,-1):
#         fact *= n
#     print(f'{num}! = {fact}')

# factorial(5)
# factorial(8)
# factorial(13)

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

num = int(input('Enter a number: '))
print(factorial(num))
# code to add two numbers

print("Code starts")
try:
    num1 = int(input('Enter the number: '))
    num2 = input('Enter the number: ')
    print(num1 - num2)

# except (ValueError, TypeError) as err:
#     print('Something went wrong ->', err)

# except BaseException as err:
#     print('Something went wrong ->', err)


finally:
    """It will execute whether the exception occurs or not its irrespective of the occurance of error"""
    print('Will execute no matter what happens')

print('Code ends')

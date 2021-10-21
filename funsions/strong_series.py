""" Basic Function of an Addition operation"""
def add():
    print(num1, num)
    return num1 + num
    
    
""" This function returns the factorial of a given number"""
def strong_op(num):
    res = 0
    while num:
        last_digit = num % 10
        fact = 1
        for n in range(1, last_digit + 1 ):
            fact *= n
        num //=10
        res += fact
    return res


def factorial(num):
    res = int()
    while num:
        res = add(res , factorial(num % 10))
        num //= 10
    return res


"""This function returns the boolean value whether the number is strong or not"""
def is_strong(num)-> bool:
    if num ==strong_op(num):
        return True
    return False


"""This function compares the count of the strong numbers with,
 the given upper limit of the strong number"""
def strong_serie(upper):
    count = int()
    num =1
    while count < upper:
        if is_strong(num):
            print(f'{num} is a strong number')
            count += 1
        num += 1
    print(count)

upper = int(input('Enter the upper limit: '))
strong_serie(upper)
"""Main function checking whether the given number is prime or not"""
def main():
    num = int(input('Enter a num: '))
    if is_prime(num):
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')


"""It takes count of factors as an input!!
    if count of factors are more than 1 it return True :: else it returns False
    """
def is_prime(num:int)-> bool:
    if count_of_factors:
        return 0
    return 1

""" It checks the number of factors between 2 and squareroot of a number and
     return the count of the factors"""
def count_of_factors(num:int)-> int:
    for n in range(2, sqrt(num)+1):
        if num % n:
            return count +1
        return count

"""Sqrt function calculates the square root of a number and 
    returns the integer value"""
def sqrt(num:int)->int:
    return int(num ** 0.5)

main()
    
       
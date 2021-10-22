def amstrong_series() :
    num = int(input('Enter the number of amstrong numbers: '))
    count = 0
    n = 1
    while count < num :
        if is_amstrong(n) :
            print(n)
            count += 1
        n += 1

def is_amstrong(num: int)->bool :
    if num == result(num) :
        return True
    return False


def result(num: int)->int :
    res = 0
    rise = num_of_digits(num)
    while num :
        digit = last_digit(num)
        res += (res, digit ** rise)
        num = division_num(num)
    return res


def num_of_digits(num: int)->int :
    count = 0
    while num :
        num = division_num(num)
        count += 1
    return count

def division_num(num: int)->int :
    return num // 10


def last_digit(num: int)->int:
    return num % 10

amstrong_series()
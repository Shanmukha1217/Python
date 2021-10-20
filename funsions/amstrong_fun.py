
def main():
    num = int(input('enter a num: '))
    is_amstrong(num)


def is_amstrong(num:int)-> bool:
    if result(num) == num:
        return print(f'{num} is a amstrong')
    return print(f'{num} is not amstrong')


def no_of_digits(num:int)->int:
    count = 0
    while num:
        num //= 10
        count += 1
    return count


def result(num:int)-> int:
    temp = num
    res = 0
    while temp:
        last_digit = temp % 10
        res += (last_digit ** no_of_digits(num))
        temp //= 10
    return res


main()
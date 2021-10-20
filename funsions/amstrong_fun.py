def main():
    res = 0
    num = int(input('enter a num: '))
    if is_amstrong(num):
        print('is amstrong')
    else:
        print('is not amstrong')

def no_of_factors(num:int)->int:
    count = 0
    while temp:
        temp //= 10
        count += 1
    return count


def result(num:int)-> int:
    temp = num
    if no_of_factors:
        while temp:
            last_digit = temp % 10
            res += (last_digit ** count)
            temp //= 10
        return res




main()
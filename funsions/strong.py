def main():
    num = int(input('Enter a num: '))
    is_strong(num)

def is_strong(num):
    if result(num) == num:
        return print('is a strong number')
    return print('is not a strong number')

def result(num):
    res = 0
    while num:
        last_digit = num % 10
        fact = 1
        for n in range(1, last_digit + 1 ):
            fact *= n
        num //=10
        res += fact
    return res


main()
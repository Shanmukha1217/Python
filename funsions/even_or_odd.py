def even_odd():
    num = int(input('Enter the number to check if it is even or odd: '))
    if num % 2:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

even_odd()
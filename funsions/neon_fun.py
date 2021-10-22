lower = int(input('Enter the lower bound of the range: '))
upper = int(input('Enter the upper bound of the range: '))

def neon (num) :
    square = num * num 
    sum = 0
    while (square != 0) : 
        sum = sum + (square % 10)
        square = square // 10
    c = (sum == num)
    return c

i = lower
print ("Neon numbers between",lower,"and",upper,"are :")
while i <= upper : 
    if (neon(i)) : 
        print(i)
    i = i + 1
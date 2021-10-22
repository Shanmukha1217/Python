
def recur_sum(n):
    if n <= 1:
        return n
    return n + recur_sum(n-1)

num = int(input('enter the number: '))
print("The sum is",recur_sum(num))
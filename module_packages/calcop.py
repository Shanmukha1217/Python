import calc as c

def main():
    print("Welcome to Calculator app")

    choice = int(input("Type \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))


    if choice >= 5:
        print('You have entered invalid input')
    else:
        num1 = int(input('enter the number to calculate: '))
        num2 = int(input('enter the numbe to claculate with: '))
        if choice == 1:
            print(f'{num1} + {num2} = {c.add(num1,num2)}')
        elif choice == 2:
            print(f'{num1} - {num2} = {c.sub(num1,num2)}')    
        elif choice == 3:
            print(f'{num1} * {num2} = {c.mul(num1,num2)}')
        else:
            print(f'{num1} / {num2} = {c.div(num1,num2)}')

if  __name__ == "__main__":
    main()
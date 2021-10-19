# if else if 
n1 = int(input('Enter first numbeer: '))
n2 = int(input('Enter second numbeer: '))
n3 = int(input('Enter third numbeer: '))


# if n1 == n2== n3:
#     print('all the tree numbers are equal')
# elif n1>n2 and n1>n3:
#     print(n1,'is greater than',n2 ,'and',n3)
# elif n2>n3:
#     print(n2,'is greater than',n1,'and',n3)
# else:
#     print(n3,'is greater than',n1,'and',n2)



# if n1 > n2 and n1 > n3:
#     print('{} greater than {} and {}'.format(n1, n2, n3))
# elif n2 > n3:
#     print('{} greater than {} and {}'.format(n2, n1, n3))
# else:
#     print('{} greater than {} and {}'.format(n3, n1, n2))



# Nested if 

if n1 < n2 or n1 < n3:
    if n2 > n3:
        print('{} greater than {} and {}'.format(n2, n1, n3))
    else:
        print('{} greater than {} and {}'.format(n3, n1, n2))
else:
    print('{} greater than {} and {}'.format(n1, n2, n3))



# Ternary operator

# print('{} greater than {} and {}'.format(n1, n2, n3)) if n1> n2 and n1>n3 else print('{} greater than {} and {}'.format(n3, n1, n2)) print('{} greater than {} and {}'.format(n2, n1, n3)) if n2 > n3 else print('all the tree numbers are equal')

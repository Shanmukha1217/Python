marks = int(input('Enter the marks: '))

if marks >90:
    print('student is graded, awesome(a)')
elif marks > 75 and marks <90:
    print('student is graded, b')
elif marks > 60 and marks <75:
    print('student is graded above average, c')  
elif marks > 35 and marks <60:
    print('student is graded average, d')
elif marks <35:
    print('The sudent failed')  
else:
    print('The sudent is pass')
def monthly_salary():
    salary = int(input('Enter the salary: '))
    no_of_working_days = int(input('Enter how many days you have to work: '))
    no_of_days_worked = int(input('Enter how many days you have worked: '))
    per_day_salary = salary / 30
    ot = no_of_days_worked - no_of_working_days
    lop = 20 - no_of_days_worked

    if no_of_days_worked > 30:
        print("you have entered the invalid input")

    elif no_of_days_worked == no_of_working_days or no_of_days_worked == 20:
        print("Hey you got the salary", salary)

    elif no_of_days_worked > no_of_working_days:
        print('you have worked extra ',ot , 'days')
        salary +=  ot* ( 2 * per_day_salary)
        print('Your salary is',salary)

    elif no_of_days_worked < 20:    
        print('you have missed',lop ,'days')
        salary -= lop * (per_day_salary)
        print('Your salary is',salary)


monthly_salary()
#conversion functions
str()
int()
float()
#input function: takes input from user and returns a string
#if conditional
x = int(input('enter a number? '))
if x>0:
    print('number x is positive')
#if else conditional
x = int(input('enter a number? '))
if x>0:
    print('number x is positive')
else:B
    print('Number is negative')
#if elif,else conditional 
#experience and salary
experience = int(input('Enter your experience \n'))
if experience >= 10:
    print('Salary is $100000')
elif experience >= 5:
    print('Salary is $50000')
elif experience >= 2:
    print('Salary is $20000')
else:
    print('Salary is $10000')
#nested if 
#number x,y compare equal,x is less than y,x is greater than y
x = int(input('Enter the value of X? \n'))
y = int(input('Enter the value of Y? \n'))
if x==y:
    print('X is Equal to Y')
else:
    if x>y:
        print('X  is greater than Y')
    else:
        print("X  is less than Y")
        

    
    
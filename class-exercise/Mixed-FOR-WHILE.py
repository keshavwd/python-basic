#Write a program to print a number pattern using loops.
'''
n = 5
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ")
    print()
'''

# Write a program to count the frequency of each character in a string.
'''
txt = 'Write a program to count the frequency of each character in a string'
li = {}
for i in txt:
    if i in li:
        li[i] += 1
    else:
        li[i] = 1
print(li)
'''

#Write a program to print all Armstrong numbers between 1 and 1000.
"""
n = 1000
for i in range(1,n):
    num = str(i)
    numlen = len(num)
    res = 0
    for num1 in num:
        res = res + int(num1)**numlen
    if numlen > 2 and i == res:
        print(f'{i} is a Armstrong number')
'''

#Write a program to simulate an ATM menu using a while loop.
'''
balance = 198337
while True:
    print("Welcome to Bla-bla Banking system")
    print('''
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    ''')
    ch = int(input("Enter the number to perform action: "))
    if ch == 1:
        print(f"Your current account balance is Rs.{balance}")
        input("Enter to continue...")
    elif ch == 2:
        val = int(input("Enter the amount you need to deposit: "))
        balance = balance + val
        print(f'Your updated balance is Rs.{balance}')
        input("Enter to continue...")
    elif ch == 3:
        val = int(input("Enter the value you need to withdraw: "))
        if val > balance:
            print(f"Your withdrawl amount is more than your balance. Please enter correct amount.")
        else:
            balance = balance - val
            print(f'Your withdrawl amount is Rs.{val} and your current balance is Rs.{balance}')
        input("Enter to continue...")
    elif ch == 4:
        print("Thank you. We are always in your service.")
        input("Enter to Exit...")
        break
    else:
        print("Wrong Entry!")
        input("Enter to continue...")
"""

#Write a program to find the GCD of two numbers using loops.
n1 = 30
n2 = 50
r = 1
while r == 0:
    r = n2%n1
    n2=n1
    n1=r
print(n1)

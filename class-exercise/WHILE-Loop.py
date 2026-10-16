#Write a program to print numbers from 1 to 50 using a while loop.
'''
n = 1
while n <= 50:
    print(n, end=" ")
    n = n+1
'''

#Write a program to print all odd numbers between 1 and 50.
'''
n = 1
while n <= 50:
    if n%2!=0:
        print(n)
    n = n+1
'''

#Write a program to calculate the sum of digits of a number.
'''
n = int(input('Enter the number to add: '))
add = 0
while n > 0:
    a = n%10
    add = add+a
    n = n//10
print(add)
'''

#Write a program to reverse a number using a while loop.
'''
n = int(input('Enter the number to add: '))
add = 0
while n > 0:
    a = n%10
    add = add*10 + a
    n = n//10

print(add)
'''

#Write a program to find the factorial of a number using a while loop.
'''
num = 8
res = 1
for i in range(1,num+1):
    res = res*i
print(res)
'''

#Write a program to keep taking input from the user until the user enters 0.
'''
while True:
    num = int(input('Enter the number: '))
    if num == 0:
        break
    print(f'The number you entered is {num}')
'''

#Write a program to find the largest digit in a number.
'''
li = [1,2,3,5,5,8,4,5,6]
i = 1
largest = li[0]
while i < len(li):
    if li[i] > largest:
        largest = li[i]
    i = i+1
print(largest)
'''

#Write a program to check whether a number is a palindrome.
'''
n = int(input("Enter the number: "))
n1 = n
res = 0
while n > 0:
    res = res*10 + n%10
    n = n//10
if n1 == res:
    print(f'{n1} is equal to {res} so it is a palindrome number')
else:
    print(f"{n1} is not equal to {res} is not a palindrome number")
'''

#Write a program to print the Fibonacci series up to n terms.
'''
n= int(input("Enter the numer: "))
li = [0,1]
i = 1
while len(li)<n:
    res = li[-1] + li[-2]
    li.append(res)
print(li)
'''

#Write a program to implement a number guessing game using a while loop.
'''
import random
snum = random.randint(1,100)
mynum = int(input("Enter the number you guess: "))
attempt = 0
while True:
    if attempt < 6:    
        if mynum < snum:
            print(f"{mynum} is smaller than the number.")
            attempt += 1
            input(f"Enter to move forward...You have {7 - attempt} left")
            mynum = int(input("Enter the number you guess: "))
        elif mynum > snum:
            print(f"{mynum} is greater than the number.")
            attempt += 1
            input(f"Enter to move forward...You have {7 - attempt} left")
            mynum = int(input("Enter the number you guess: "))
        else:
            print(f'Congratulation. {mynum} is the correct guess.')
            input("Enter to move forward...")
            break
'''

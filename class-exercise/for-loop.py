#Write a program to print numbers from 1 to 100.
'''
i = 0
for i in range(0,100):
    i = i+1
    print(i)
'''

#Write a program to print all even numbers between 1 and 50.
'''
i = 0
for i in range(1,51):
    if i%2==0:
        print(i)
    i = i+1
'''

#Write a program to print the sum of first n natural numbers.
'''
n = int(input('Enter the number to add : '))
add = 0
for i in range(1,n+1):
    add = add+i
print(add)
'''

#Write a program to print the multiplication table of a given number.
'''
n = 5
for i in range(1,11):
    print(f'{n}*{i}=',n*i)
'''

#Write a program to print all elements of a list using a for loop.
'''
li = ['a', 1, 'b', 2, 'c', 3]
for i in li:
    print(i)
'''

#Write a program to count the number of vowels in a string.
'''
txt = 'Hello world'
ch = 'aeiouAEIOU'
for i in txt:
    if i in ch:
        print(i)
'''

#Write a program to find the largest number in a list.
'''
li = [1,2,3,5,6,8,9,55,33,22,33]
num = 0
for i in li:
    if i > num:
        num = i
print(num)
'''

#Write a program to print all prime numbers between 1 and 100.
'''
n = 100
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i ,end=' ')
'''


#Write a program to calculate the factorial of a number using a for loop.
'''
n = 5
res = 1
for i in range(1,5+1):
    res = res*i
print(res)
'''     

#Write a program to print the reverse of a string using a for loop.
txt = "Hello World"
'''
txtrev = txt[::-1]
print(txtrev)

txtlen = len(txt)
for i in range(txtlen-1,-1,-1):
    print(txt[i],end="")
'''

#https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
#Print first 10 natural numbers using while loop
'''
n = 1
while n <=10:
    print(n)
    n += 1
'''

#Display numbers from -10 to -1 using for loop
'''
for i in range(-10,0,1):
    print(i)
'''

#Display a message “Done” after successful execution of for loop
'''
for i in range(0,5):
    print( i)
else:
    print("Done")
'''

#Calculate the sum of all numbers from 1 to N
'''
num = int(input("Enter the last digit for sum from 0 to: "))
s = 0
s1 = 0
count = 0
while count <= num:
    s = s+count
    count += 1
print(s)

for i in range(num+1):
    s1 +=i
print(s1)
'''

#Print multiplication table of a given number
'''
n = int(input("Enter the number to have the table: "))
for i in range(1,10+1):
    print(f"{n}*{i}={n*i}")
'''

#Calculate the cube of all numbers from 1 to a given number
'''
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(f"Current Number is : {i} and the cube is {i**3}")
'''

#Display numbers from a list using a loop
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i >500:
        break
    if i > 150:
        continue
    if i%5==0:
        print(i)
'''

#Count occurrences of a specific element in a list
'''
list1 = [10, 20, 10, 30, 10, 40, 50]
tar = 10
count = 0
for i in list1:
    if i == tar:
        count += 1
print(count)
'''

#Print elements from a list present at odd index positions
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
nlist = []
for i in range(len(my_list)):
    if i%2!=0:
        nlist.append(my_list[i])
print(nlist)
'''

#Print list in reverse order using a loop
'''
list1 = [10, 20, 30, 40, 50]
res = []
for i in range(len(list1),0,-1):
    res.append(list1[i-1])
print(res)
'''

#Reverse a string using a for loop (no slicing)
s = "Python"
'''
s1=s[::-1]
print(s1)
'''
'''
s1 = ""
for ch in s:
    s1 = ch + s1
print(s1)
'''

#Count vowels and consonants in a sentence
'''
s = "Loops are Fun!"
vovel = "aeiou"
cons = 0
vov = 0
for ch in s.lower():
    if ch.isalpha():
        if ch in vovel:
            vov += 1
        else:
            cons += 1
print(vov, "count")
print(cons, "count")
'''

#Count total number of digits in a number
'''
n = int(input("Enter the digits: "))
count = 0
while n > 0: 
    #print(12345//10)
    res = n//10
    count += 1
    n = res
'''

#Reverse an integer number
'''
n = 76542
res = 0
while n > 0:
    va = n%10
    res = (res*10)+va
    n = n//10
    
print(res)
'''

#Find largest and smallest digit in a number
'''
num = 75869
li = []
ma = 0
mi = 0
while num > 0:
    li.append(num%10)
    num = num//10

a = 0
b = 9
for n in li:
    if n > a:
        a = n
    elif n < b:
        b = n
print(f"Max: {a} and Min: {b}")
'''

#Check if a number is a palindrome
'''
num1 = int(input("Enter the number: "))
num = num1
res = 0
while num > 0:
    res = (res*10)+num%10
    num = num//10
if num1 == res:
    print(f"Number is palindrome NUM: {num1} and RES: {res}")
else:
    print(f"Number is not palindrome NUM: {num1} and RES: {res}")
'''

#Find factorial of a number
'''
num = int(input("Enter the number to get factorial: "))
sp = 1
if num < 0:
    print("Factorial doesnot exist for a negative number.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1,num+1):
        sp = sp*i
    print(f"Factorial for {num} is {sp}.")
'''

#Collatz Conjecture: Generate a sequence until it reaches 1
'''
n = 6
li = [n]
while n > 1:
    if n%2==0:
        n = n//2
        #print(n)
        li.append(n)
    else:
        n = (n*3)+1
        #print(n)
        li.append(n)
print(li)
'''

#Armstrong Number Check (for a 3 digi number the sum of cube of each digit is same as the 3 digit number)
'''
n = int(input("Enter the number: "))
n1 = n
nlength = len(str(n1))
total = 0
while n1>0:
    d = n1%10
    total += d**nlength
    n1 = n1//10
if n == total:
    print(f"Number {n} is Armstrong Number.")
else:
    print(f"Number {n} is not an Armstrong Number.")
'''

#Print right-angled triangle Number Pattern using a Loop
'''
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''

#Print the decreasing pattern
'''
n = 5
for i in range(n,0,-1):
    #print(i)
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
'''

#Print the alternate numbers pattern
'''
n = 20
for i in range(1,20,2):
    print(i,end=" ")
'''

#Print Alphabet pyramid (A, BB, CCC) pattern
#A = 65 and a = 97
'''
num = 65
counter = 1
for i in range(65,65+5):
    print(chr(i )*counter)
    counter += 1
'''

#Hollow square pattern
'''
n = 5
t = "*"
for i in range(0,5):
    for j in range(0,5):
        if i>0 and i<4 and j>0 and j<4:
            print(" ",end=" ")
        else:
            print(t,end=" ")
    print()
'''

#Print pyramid pattern of stars
'''
n = int(input("Enter the number of row to print: "))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(0,i):
        print("*",end=" ")
    print()
'''

#Print full multiplication table (1 to 10)
'''
n = 10
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end="\t")
    print()
'''

#List Cumulative Sum: Each element is the sum of all previous
'''
l1 = [1, 2, 3, 4]
l2 = []
res = 0
for i in l1:
    res = res+l1[i-1]
    l2.append(res)
print(l2)
'''

#Dictionary Filter: Extract pairs where value exceeds a threshold.
'''
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} #threshold = 75
for key,value in scores.items():
    #print(value)
    if value > 75:
        print(key,value)
'''

#Find common elements (Intersection) using loop
'''
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
li = []
for i in list_a:
    if i in list_b:
        li.append(i)
print(li)
'''

#Remove duplicates without set
'''
li = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 6, 6]
li1 = []
for i in li:
    if i in li1:
        continue
    else:
        li1.append(i)
print(li1)
'''

#Even/Odd Segregation: Move evens to front, odds to back
li = [1, 2, 3, 4, 5, 6]

#Condition result
'''
while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res1 = num1 * num2
    res2 = num1 + num2
    if res1 <= 1000:
        print(res1)
    else:
        print(res2)
'''

#Sum
'''
i = 0
while i<10:
    #res = i
    #sum for current and previous number if exist
    #sum =
    #print(i)
    res = i+(i-1)
    if res < 0:
        print(0)
    else:
        print(res)
    
    i=i+1
'''

#print event from string
'''
str = "pynative"
count = 0
for i in str:
    #print(count, i)
    if (count+1)%2==0:
        print(i)
    count = count+1
'''

#Truncate string
'''
str = input("Enter the word or paragraph to truncate: ")
strfs = int(input("Remove characters from start: "))
strfe = int(input("Remove characters from end: "))
count = 0
for i in str:
    count = count+1
print(str)
if strfs < count-1:
    print(str[strfs:])
else:
    print(f"Please enter value less than {count}")
    
if strfe < count-1:
    print(str[:strfe])
else:
    print(f"Please enter value less than {count}")
'''

#Value swapping without third variable
'''
a = 5
b = 8
c = 9
print(a,b,c)
a, b, c = c, b, a
print(a,b,c)
'''

#Factorial
'''
num = int(input("Enter fact number: "))
res = 1
for i in range(1,num+1):
    res = res*i
print(res)
'''

#List Manipulation: Add and Remove
#fruits["apple", "banana", "cherry", "date", "elderberry"]
#['apple', 'cherry', 'date', 'elderberry', 'fig']
'''
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.pop(1)
fruits.append('fig')
print(fruits)
'''

#String Reversal
'''
text = "Python"
print("".join(reversed(text)))
'''
'''
text = "Python"
print(text[::-1])
'''
#Vowel Frequency Counter
'''
sentence = "Learning Python is fun!"
counter = 0
for i in sentence:
    if i.lower() in 'aeiou':
        counter += 1
print(counter)
'''

#Finding Extremes (Min/Max) in a List
'''
nums = [45, 2, 89, 12, 7]

print(max(nums), min(nums))
'''

#Removing Duplicates from a List
'''
data = [1, 2, 2, 3, 4, 4, 4, 5]
print(set(data))
'''

#List Comparison and Boolean Logic
'''
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def comboolean(x):
    fnum = x[0]
    snum = x[-1]
    if fnum == snum:
        print("First and last index numbers are same")
        return True
    else:
        print("First and last index numbers are not same")
        return False

comboolean(numbers_x)
comboolean(numbers_y)
'''

#Filtering Lists with Conditional Logic
'''
num_list = [10, 20, 33, 46, 55]
print("Numbers divisi ble by 5 are:")
for i in num_list:
    if i%5==0:
        print(i)
'''

#Substring Frequency Analysis
'''
str_x = "Emma is good developer. Emma is a writer"
ch = str_x.count("Emma")
print(ch)
'''

#Nested Loops for Pattern Generation
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
'''
for i in range(0,5):
    print()
    for j in range(0,i+1):
        print(i+1,end=' ')
'''

#Numerical Palindrome Check
'''
ch = int(input("Enter number to check if number is palindrome: "))
print(ch)
ch = str(ch)
if ch == ch[::-1]:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
'''

#Merging Lists with Parity Filtering
'''
Create a new list from two given lists such that the new list contains odd
numbers from the first list and even numbers from the second list.'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
'''
#solution 1
listf = []
for n in list1:
    if n%2==0:
        listf.append(n)

for n in list2:
    if n%2!=0:
        listf.append(n)
print(listf)
'''
'''
#solution 2
def listm(list1,list2):
    listf = []
    for n in list1:
        if n%2==0:
            listf.append(n)

    for n in list2:
        if n%2!=0:
            listf.append(n)
    return listf

print("New list is ",listm(list1,list2))
'''

#Integer Digit Extraction and Reversal
'''
number = int(input("Enter thr desired number: "))
dv = int(input("Enter thr desired number from which you divide and should be divisible of 10: "))
print(number)
while number > 0:
    #print the digit from right
    d = number % dv
    #reassigning value to number by removing number after decimal
    number = number//dv
    print(d)
'''

#Multi-Tiered Income Tax Calculation
#For an income of 45,000: the first 10k is free,
#the next 10k is taxed at 10% (1,000), and the remaining 25k is taxed at 20% (5,000)
'''
while True:
    income = int(input("Enter the salary: "))
    if income <= 10000:
        tax = 0
        print(tax)
    elif income <=20000:
        tax = (10/100)*(income - 10000)
        print(tax)
    else:
        tax = ((20/100)*((income - 20000)))+1000
        print(tax)
'''

#Nested Loops for Multiplication Tables
#Print a multiplication table from 1 to 10 in a formatted grid.
'''
i = 1
while i <= 10:
    print()
    for j in range(1,11):
        print(j*i,end="\t")
    #print(i)
    i+=1
'''

#Downward Half-Pyramid Pattern
#Print a downward half-pyramid pattern using stars (*).
'''
a = "*"
for i in range(6,1,-1):
    print()
    for j in range(1,i):
        print(a,end=" ")
'''

#Custom Exponentiation Function
'''
base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = 1
while exp > 0:
    result = result * base
    exp = exp-1
print(result)
'''

#Check Palindrome Number
'''
num = int(input("Enter the number: "))
num2 = int(input("Enter the number to divide: "))
num1 = num
res1=[]
while num1 > 0:
    res = num1%num2
    #print(res)
    num1 = num1//num2
    res1.append(res)
res1 = int("".join(map(str,res1)))
print(num, res1)
status = "Number is Palindrome" if res1 == num else "Number is not Palindrome"
print(status)
'''

#Generate Fibonacci Series
#doubt
'''
n1 = 0
n2 = 1
r = 15
while r > 1:
    res = n1 + n2
    n1 = n2
    n2 = res
    r = r-1
print(res)
'''
#Check Leap Year
'''
while True:
    y = int(input("Enter the year: "))
    print("Leap year" if (((y%4==0) and (y%100!=0)) or y%400 == 0) else "Not a leap year")
'''

#Merging Two Dictionaries
'''
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
print("Sol 1", dict1 | dict2)
dict1.update(dict2)
print("Sol 2", dict1)
merg = {**dict1, **dict2}
print("Sol 3", merg)
'''

#Finding Common Elements (Intersections)
'''
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
list_1 = set(list_a)
list_2 = set(list_b)
print(list_1 & list_2)
'''

#Odd/Even List Splitter
'''
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
numbers.reverse()
odd=[]
even=[]
n=len(numbers)
#print(len(numbers))
while n > 0:
    n = n-1
    if numbers[n]%2==0:
       even.append(numbers[n])
    else:
        odd.append(numbers[n])
print(even)
print(odd)
'''

#Word Length Analysis
'''
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
wlist = []
for word in words:
    print(f"{word} - {len(word)}",end=" ")
'''

#Word Frequency Counter (The Histogram)
'''
text = "apple banana apple cherry banana apple"
words = text.split(" ")
data = {}
for i in words:
    if i in data:
        data[i] = data[i]+1
    else:
        data[i] = 1
'''

#Print Alternate Prime Numbers
'''
ntill = 20
np = 0
for i in range(2,20+1):
    print("Number",i)
    for multiple in range(1,i+1):
        if i%multiple==0:
            print("Inner",i)
'''
'''
def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True

while True:
    n = int(input("Enter the integer: "))
    for n in range(2,n):
        print(is_prime(n), n)
'''

#Dictionary of Squares (Mapping Logic)
#Create a dictionary where the keys are numbers
#from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9)
'''
sq = {}
for i in range(1,10):
    sq[i]=i*i
print(sq)
'''

#Character Replacer (Data Sanitization)
'''
stri = str(input("Enter the string: "))
res = stri.replace(" ","_")
print(res)
'''

#Print Reverse Number Pattern
'''
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    #print((n+1)-i)
    print()
'''

#Digit Detection in Strings
'''
input_string = str(input("Enter your desired content: "))
for ch in input_string:
    if ch.isdigit():
        print(ch)
'''

#Capitalize First Letter (Title Case)
'''
text = "hello world from python"
print(text.title())
'''
'''
text = "hello world from python"
t2 = []
for ch in text.split():
    t2.append(ch.capitalize())
text = " ".join(t2)
print(text)
'''

#Simple Countdown Timer
'''
import time
start_count = 5
while start_count > 0:
    print(start_count)
    start_count -= 1
    time.sleep(1)
print("Blast off!")
'''

#File Creation and Basic I/O
'''
with open("notes.txt",'w') as file:
    file.write("Hello, this is my first note.\n")
    file.write("Python file handling is simple.\n")
    file.write("End of file...")
print("Reading the file content")
with open("notes.txt","r") as filess:
    content = filess.read()
    print(content)
'''
#External File Word Counter
'''
try:
    with open("notes.txt","r") as file:
        content = file.read()
        count = 0
        for ch in content.split():
            if ch:
                count += 1
        print(count)
except:
    print("File you are searching is not found.")
'''

#Introduction to Classes (OOP)
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def starteng(self):
        print(self.make, self.model, self.year)

my_car = Car("Tata","Nexon",2026)
my_car.starteng()
'''
class MyClass:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def myFunc(self):
        print(self.name, self.age, self.gender)

myfun = MyClass("Keshav", 30, "Male")
myfun.myFunc()

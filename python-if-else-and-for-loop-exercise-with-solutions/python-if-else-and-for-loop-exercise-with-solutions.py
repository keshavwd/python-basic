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

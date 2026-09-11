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
list1 = [10, 20, 30, 40, 50]

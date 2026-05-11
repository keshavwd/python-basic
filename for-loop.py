#PART 1 – Basic For Loop Questions 
#Q1. Print Numbers 
#Use a for loop to print numbers from 1 to 10.
'''
for i in range(1,11):
    print(i)
'''
#Q2. Print Even Numbers 
#Print all even numbers between 1 and 20.
'''
for j in range(1,21):
    if j%2==0:
        print(j)
'''
#Q3. Find Sum 
#Print the sum of numbers from 1 to 10 using a for loop.
'''
j = 0
for i in range(1,11):
    j = j+i
print(j)
'''
#Q4. Multiplication Table 
#Take a number from the user and print its multiplication table up to 10.
'''
num = int(input("Enter the number : "))
for i in range(1,11):
    print(num*i)
'''   

#Q5. Count Characters 
#Take a string and count the total number of characters using a for loop.
'''
text = str(input("Enter text : "))
j = 0
for i in text:
    j = j+1
print(j)
'''
#PART 2 – Break Related Questions

#Q6. Stop at 5 
#Print numbers from 1 to 10. 
#Stop the loop when the number becomes 5.
'''
for i in range(1,11):
    if i == 5:
        break
    print(i)
'''

#Q7. Search in List 
#Search for number 25 in a list. 
#If found, print "Found" and stop the loop.
'''
li = [23, 34, 23, 45, 25, 45]
for i in li:
    print("loop is running ",i)
    if i == 25:
        break
print(i," found in list")
'''
#Q8. First Negative Number 
#Given a list of numbers, print the first negative number and stop the loop.
'''
li = [23, 34, 23, -45, 25, 45]
for i in li:
    print("loop is running ",i)
    if i < 0:
        break
print(i," found in list")
'''

#PART 3 – Continue Related Questions 
#Q9. Skip 5 
#Print numbers from 1 to 10. 
#Skip number 5.
'''
for i in range(1,11):
    if i == 5:
        continue
    print(i)
'''

#Q10. Skip Even Numbers 
#Print numbers from 1 to 20. 
#Skip all even numbers.
'''
for i in range(1,21):
    if i%2 == 0:
        continue
    print(i)
'''


#Q11. Skip Letter 
#Print each character of the string "PYTHON". 
#Skip the letter "O".
'''
text = "PYTHON"
for i in text:
    if i == 'O':
        continue
    print(i)
'''
#PART 4 – Pass Related Questions 
 
#Q12. Empty Loop 
#Run a loop from 1 to 5 but do nothing inside the loop using pass.
'''
for i in range(1,5):
    pass
'''
#Q13. Skip Using Pass 
#Loop from 1 to 10.
#If number is 6, just use pass.
'''
for i in range(1,11):
    if i == 6:
        pass
    print(i)
'''

'''
 

 
PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.) 
 
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found". 
 
Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else. 
'''
#PART 6 – Pattern Questions 
 
#Q16. Star Pattern 
#Print: 
'''
* 
** 
*** 
**** 
***** 
'''
'''
a = '*'
for i in range(1,6):
    print(a*i,end="")
    print()
'''
#Q17. Reverse Star Pattern
'''
Print: 
***** 
**** 
*** 
** 
*
'''
'''
a = '*'
for i in range(1,6):
    print(a*(6-i),end="")
    print()
'''
#Q18. Number Pattern
'''
Print: 
1 
12 
123 
1234 
12345 
'''
'''
a = 1
for i in range(1,6):
    for j in range(i):
        print(j+1,end="")
    print()
'''
#Q19. Same Number Pattern
'''
Print: 
1 
22 
333 
4444 
55555 
'''
'''
a = 1
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
'''


#Q20. Pyramid Pattern
'''
Print: 
        * 
      *** 
    ***** 
  ******* 
********* 
'''
'''
a = "*"
for i in range(1,10,2):
    print(" "*(10-i),end="")
    print("*"*(i))
'''

#Q21. Inverted Pyramid
'''
Print: 
********* 
  ******* 
    ***** 
      *** 
        *
'''
'''
a = "*"
for i in range(1,10,2):
    print(" "*(i),end="")
    print("*"*(10-i),end="")
    print()
'''
'''
 
Bonus Question 
Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.
'''
for i in range(1,11):
    print(('*')*(11-1),end="")
    if i == 4:
        break
    print()

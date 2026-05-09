#B. Python IF–ELSE (Two Conditions) 
#11. Check whether a number is even or odd.
num = int(input("Insert the number : "))
if num%2 == 0 :
    print("Even number")
else:
    print("Odd number")
#12. Find the largest of two numbers.
num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
if num1 > num2 :
    print(num1, "is greater")
else:
    print(num2, "is greater")
#13. Check whether a person is eligible for driving license.
age = int(input("Enter the age : "))
if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")
#14. Print "Pass" or "Fail" based on marks.
marks = int(input("Enter the marks : "))
if marks > 40:
    print("Pass")
else:
    print("Fail")
#15. Check whether a number is positive or negative.
num3 = int(input("Enter the number : "))
if num3 > 0:
    print("Number is positive")
else:
    print("Number is negative")
#16. Check whether a character is a vowel or consonant.
char = str(input("Enter the character : "))
if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(char, 'is vovel')
elif char.isalpha():
    print(char, 'is consonant')
else:
    print("Not a alphabet")
#17. Check if a year is leap or not.
year = int(input("Enter the year : "))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print("Not a leap year")
#18. Print "Valid Password" or "Invalid Password".
pass = str(input("Enter the password : "))
if pass == 'admin@123':
    print("Valid Password")
else:
    print("Invalid Password")
#19. Determine whether salary is taxable or not.
sal = float(input("Enter your salary : "))
if sal > 500000:
    print("Salary is taxable")
else:
    print("Not taxable")
#20. Check whether a number is greater than 50 or not.
num4 = int(input("Enter the number : "))
if num4 > 50:
    print("Number is greated than 50")
else:
    print("Number is not greater than 50")

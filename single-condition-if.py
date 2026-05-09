#A. Python IF (Single Condition) 
#1. Write a Python program to check if a number is positive.
num1 = int(input("Insert the number : "));
if num1 > 0:
    print('Ni=umber is positive')
#2. Print "Eligible to vote" if age is 18 or above.
age = int(input("Insert the age : "))
if age >= 18 :
    print("Eligible to vote")
#3. Check if a number is divisible by 7.
num2 = int(input("Insert the number : "))
if num2 % 7 == 0 :
    print("number is divisible by 7")
#4. Print "Pass" if marks are greater than 40.
num3 = int(input("Enter the marks : "))
if num3 > 40 :
    print("Pass")
#5. Check if a number is greater than 100.
num4 = int(input("Insert the number : "))
if num4 > 100 :
    print("Number is greater than 100")
#6. Display a message if temperature exceeds 45°C.
temp = float(input("Insert the temprature : "))
if temp > 45 :
    print("Its a hot day")
#7. Check if a string length is more than 8 characters.
text = str(input("Insert the text : "))
if len(text) > 8 :
    print("Length is more than 8")
#8. Print "Logged In" if password matches "admin123".
pass = input("Enter the password : ")
if pass == "admin123" :
    print("Logged in")
#9. Check if a number is a multiple of 10.
num5 = int(input("Enter the number : "))
if num5 % 10 == 0 :
    print("Number is multiple of 10")
#10. Print a warning if balance is below minimum limit.
bal = float(input("Enter your balance : "))
if bal < 1000 :
    print("Please maintain your balance. Your balance is less than min limit.")

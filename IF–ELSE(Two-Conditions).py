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
    print(ch, 'is vovel')
elif ch.isalpha():
    print(ch, 'is consonant')
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
sal = float(int("Enter your salary : "))
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
#C. Python NESTED IF–ELSE 
#21. Find the largest of three numbers. 
#22. Check whether a number is positive, negative, or zero. 
#23. Assign grades: 
#● A → marks ≥ 90 
#● B → marks ≥ 75 
#● C → marks ≥ 60 
#● Fail → below 60 
#24. Check whether a triangle is equilateral, isosceles, or scalene. 
#25. Check whether a character is uppercase, lowercase, digit, or special character. 
#26. Calculate electricity bill using slab-wise rates. 
#27. Validate login using username and password. 
#28. Check student result using marks of 3 subjects. 
#29. Find the second largest number among three numbers. 
#30. Check loan eligibility using age, salary, and credit score. 
#D. Python ELIF (Multiple Conditions) 
#31. Print day name using day number (1–7). 
#32. Print month name using month number. 
#33. Display grade based on percentage. 
#34. Display bonus percentage based on experience years. 
#35. Identify traffic signal meaning. 
#36. Categorize temperature as Cold / Warm / Hot. 
#37. Categorize employee based on salary range. 
#38. Print discount percentage based on purchase amount. 
#39. Identify number type: single-digit / double-digit / multi-digit. 
#40. Assign performance rating: Poor / Average / Good / Excellent. 
#E. Python COMPLEX CONDITIONS (AND / OR / NOT) 
#41. Check whether a number is divisible by 5 and 11. 
#42. Check if a person is eligible for loan: 
#● age ≥ 21 
#● salary ≥ 25,000 
#● credit score ≥ 700 
#43. Validate login using username AND password. 
#44. Check student pass condition: 
#● All subjects ≥ 40 
#● Average ≥ 50 
#45. Check if a number lies between 10 and 100. 
#46. Check exam eligibility: 
#● attendance ≥ 75% OR 
#● medical certificate available 
#47. Validate a date using conditions. 
#48. Check whether an email format is valid. 
#49. Determine insurance eligibility using age, health status, and income. 
#50. Check leap year using complete leap year logic. 
#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS 
#51. Write a Python program to calculate income tax using slabs. 
#52. Create an ATM withdrawal program with balance checks. 
#53. Check promotion eligibility using experience and performance. 
#54. Implement a grading system using nested if–else. 
#55. Validate strong password using multiple conditions. 
#56. Calculate delivery charges based on location and order amount. 
#57. Determine online exam qualification. 
#58. Create movie ticket pricing logic based on age & show time. 
#59. Determine bank account type based on balance. 
#60. Create a menu-driven program using if–elif–else. 

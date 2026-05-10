#E. Python COMPLEX CONDITIONS (AND / OR / NOT)

#41. Check whether a number is divisible by 5 and 11.
num = int(input("Insert a number : "))
if num%5 == 0 and num%11 == 0:
    print("number is divisible by 5 and 11")
elif num%5 == 0 or num%11 == 0:
    print("number is divisible by one number")
else:
    print("number is not divisible by 5 and 11")
#42. Check if a person is eligible for loan: 
#● age ≥ 21 
#● salary ≥ 25,000 
#● credit score ≥ 700
age = int(input("Insert age : "))
salary = int(input("Insert salary : "))
credit_score = int(input("Insert credit score : "))
if age > 21 and salary > 25000 and credit_score > 650:
    print("person is eligible for loan")
else:
    print("person is not eligible for loan")
#43. Validate login using username AND password.
username = str(input("Insert username : "))
password = str(input("Insert password : "))
if username == "admin" and password == "admin@123":
    print("Login")
else:
    print("Incorrect creds")
#44. Check student pass condition: 
#● All subjects ≥ 40 
#● Average ≥ 50
subject1 = int(input("Insert subjects1 marks : "))
subject2 = int(input("Insert subjects2 marks : "))
subject3 = int(input("Insert subjects3 marks : "))
average = (subject1 + subject2 + subject3)/3
if subject1 > 40 and subject2 > 40 and subject3 > 40:
    if average > 50:
        print("Pass")
    else:
        print("Fail. Average is less than 50")
else:
    print("Fail. Marks less than min marks")
#45. Check if a number lies between 10 and 100.
num1 = int(input("Insert a number : "))
if num1 > 10 and num < 100:
    print('number lies between 10 and 100')
else:
    print('number do not lies between 10 and 100')
#46. Check exam eligibility: 
#● attendance ≥ 75% OR 
#● medical certificate available
att = int(input("Enter attendance %age between 1 to 100 : "))
medical = str(input("medical certificate available Y or N : "))
if att >75 or (medical == 'Y' and att < 75 and att > 0):
    print("eligible")
else:
    print("not eligible")
    
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

#C. Python NESTED IF–ELSE
#21. Find the largest of three numbers.
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
if a > b and b > c:
    print(a,"is the largest")
elif b > a and a > c:
    print(b,'is the largest')
else:
    print(c,"is the largest")
#22. Check whether a number is positive, negative, or zero.
n = int(input("Enter the number : "))
if n > 0:
    print(n, 'is positive')
elif n < 0:
    print(n, 'is -ve')
else:
    print('It is zero')
#23. Assign grades: 
#● A → marks ≥ 90 
#● B → marks ≥ 75 
#● C → marks ≥ 60 
#● Fail → below 60
marks = int(input("Enter marks : "))
if marks >= 90:
    print('A grade')
elif marks >= 75:
    print('B grade')
elif marks >= 60:
    print('C grade')
else :
    print('Fail')
#24. Check whether a triangle is equilateral, isosceles, or scalene.
s1 = int(input("Side A : "))
s2 = int(input("Side B : "))
s3 = int(input("Side C : "))
if s1 == s2 == s3:
    print('equilateral Triangle')
elif s1 == s2 or s2 == s3 or s3 == s1:
    print('isosceles Triangle')
else:
    print('scalene Triangle')
    
#25. Check whether a character is uppercase, lowercase, digit, or special character.
chrinput = ord(input("Enter the character : "))
print(chrinput)
if chrinput >= 65 and chrinput<= (65+25):
    print("Uppercase")
elif chrinput >= 97 and chrinput<= (97+25):
    print("Lowercase")
elif chrinput >= 48 and chrinput<= (48+9):
    print("Number")
else:
    print("Its is a symbol or special character")

#26. Calculate electricity bill using slab-wise rates.
el = int(input("Enter consumed unit : "))
if el > 1000:
    print("Your bill is : ", el*12)
elif el > 500:
    print("Your bill is : ", el*10)
elif el > 200:
    print("Your bill is : ", el*8)
else:
    print("Your bill is : ", el*5)
#27. Validate login using username and password.
passw = input("Enter the password : ")
if passw == 'pass@321':
    print("Logged in")
else:
    print("Enter correct password")
#28. Check student result using marks of 3 subjects.
ma = int(input("Enter marks s1 : "))
mb = int(input("Enter marks s2 : "))
mc = int(input("Enter marks s3 : "))
tmarks = ma + mb + mc
if ma < 45:
    print("Fail")
elif mb < 45:
    print("Fail")
elif mc < 45:
    print("Fail")
else:
    print("Pas. And your result is : ", tmarks/3,'%')
#29. Find the second largest number among three numbers.
if a > b > c:
    print(b, "is the second largest")
elif b > c > a:
    print(c, "is the second largest")
else:
    print(a, "is the second largest")
    
#30. Check loan eligibility using age, salary, and credit score.
age = int(input("Enter the age : "))
salary = int(input("Enter the salary : "))
cs = int(input("Enter your cibil score : "))
if age < 18 :
    print("Not Eligible for loan")
elif salary < 15000 :
    print("Not Eligible for loan")
elif cs < 650 :
    print("Not Eligible for loan")
else:
    print("Eligible for foan")

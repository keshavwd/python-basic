#D. Python ELIF (Multiple Conditions)
#31. Print day name using day number (1–7).
day = int(input("Enter the day number from 1-7 : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thrusday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid number")
#32. Print month name using month number.
month = int(input("Enter the month number from 1-12 : "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid number")
#33. Display grade based on percentage.
percentage = float(input("Enter yor percentage : "))
if percentage > 90:
    print("Grade A")
elif percentage > 70:
    print("Grade B")
elif percentage > 50:
    print("Grade C")
else:
    print("Fail. Grade D")
#34. Display bonus percentage based on experience years.
salary = int(input("Enter your salary : "))
exp = int(input("Enter your experience : "))
if exp < 3:
    print("Your bonus is ", (salary/100)*5)
elif exp < 5:
    print("Your bonus is ", (salary/100)*7)
else :
    print("Your bonus is ", (salary/100)*10)

#35. Identify traffic signal meaning.
color = str(input("Enter the color : "))
color = color.capitalize()
if color == "Red":
    print("Red stands for STOP.")
elif color == "Yellow":
    print("Yellow stands for Ready")
elif color == "Green":
    print("Green stands for Go")
else:
    print("Enter the right color")
#36. Categorize temperature as Cold / Warm / Hot.
temp = int(input("Enter the temprature : "))
if temp > 45:
    print("Its hot")
elif temp > 25:
    print("Warm")
else:
    print("Its cold")
#37. Categorize employee based on salary range.
sal = int(input("Enter your salary : "))
if sal > 50000:
    print("Group A")
elif sal > 40000:
    print("Group B")
elif sal > 30000:
    print("Group C")
else :
    print("Group D")
#38. Print discount percentage based on purchase amount.
purchase = int(input("Enter MRP : "))
if purchase >= 2500:
    discount = 20
elif purchase >=1000:
    discount = 10
else:
    discount = 5

print(f'{discount}%')

#39. Identify number type: single-digit / double-digit / multi-digit.
num = int(input("Insert the number : "))
numL = len(str(num))
if numL == 1:
    print("SIngle digit")
elif numL == 2:
    print("double digit")
else:
    print("multi digit")
#40. Assign performance rating: Poor / Average / Good / Excellent.
performance = float(input("Enter yor marks : "))
if performance > 90:
    print("Excellent")
elif performance > 70:
    print("Good")
elif performance > 50:
    print("Average")
else:
    print("Poor")
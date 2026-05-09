#Basic Input & Print Questions
#1. Write a program to print “Hello Python” on the screen.
print("Hello Python")
#2. Take a name as input and print 
#Welcome <name>
name = str(input("Type your name : "))
print("Welcome ", name)
#3. Take a number as input and print it.
num = int(input("Enter the number : "))
print("Entered number is", num)
#4. Take two numbers as input and print both numbers on separate lines.
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
print("Entered nmber 1 is :", num1)
print("Entered nmber 2 is :", num2)
#5. Take a name and age as input and print: 
#My name is ___ and my age is ___
name1 = str(input("Enter your name : "))
age = int(input("Enter your age : "))
print("My name is", name1, 'and my age is', age)
#Integer (int) Based Questions 
#6. Take an integer as input and print its square.
int1 = int(input("Insert the number : "))
print('print its square of',int1, ' : ', int1 * int1)
#7. Take two integers as input and print their sum.
int2 = int(input("Enter the number : "))
int3 = int(input("Enter the number : "))
print('Sum of integer', int2, ' and ', int3, 'is : ',int2 + int3)
#8. Take two integers and print: 
#o Addition
print('Sum of integer', int1, ' and ', int3, 'is : ',int1 + int3)
#o Subtraction
print('Subtraction of integer', int2, ' and ', int3, 'is : ',int2 - int3)
#o Multiplication
print('Multplication of integer', int2, ' and ', int3, 'is : ',int2*int3)
#9. Take a number and print: 
#The number entered is <number>
print("The number entered is", int2)
#10. Take an integer and print its double.
print('Double of integer', int3, 'is : ',int3*2)
#Float (float) Based Questions
fl1 = float(input("Insert float value 1 : "))
fl2 = float(input("Insert float value 2 : "))
#11. Take a float value as input and print it.
print('Inserted float value as input is : ', fl1)
#12. Take two float numbers and print their sum. 
print('Sum of float value is : ', fl1 + fl2)
#13. Take a float number and print its half value. 
print('Half of float value ',fl2,' is : ', fl2/2)
#14. Take length and width (float) as input and print the area of a rectangle.  (length*width)
print('Area of rectangle whose length', fl1, 'and breadth is', fl2,'. Its area is', fl1*fl2)
#15. Take radius as float input and print the area of a circle 
#(Use π = 3.14)
print("Area of circle whose radius is", fl2, "is : ", 3.14*(fl2 * fl2))
#Mixed int & float Questions 
#16. Take one integer and one float as input and print both.
print('Take one integer', int2, 'and one float', fl1, 'as input and print both : ', int2, ' and ' ,fl1)
#17. Take total marks (int) and number of subjects (int) and print the average as float.
tm = int(input("Total marks : "))
ts = int(input("Total subject : "))
print('Average marks : ', (tm/ts))
#18. Take price (float) and quantity (int) and print the total cost.
price = float(input("Price of item is : "))
quantity = int(input("Quantity is :"))
tc = price*quantity
print('total cost of items is : ', tc)
#19. Take two numbers (one int, one float) and print their sum.
print('two numbers (one int, one float) and print their sum', int2+fl2)
#20. Take salary (float) and bonus (int) and print the final salary.
ts = float(input("Take salary : "))
bo = int(input("Bonus : "))
fs = ts + bo
print('the final salary is : ',fs)


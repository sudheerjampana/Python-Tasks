#1.Write a Python program that takes an integer as input and prints whether it is even or odd.
num=int(input("enter the number: "))
if num%2 ==0:
    print(num," is an even number.")
else :
    print(num,"is odd number")


#2.Write a program that takes two numbers as input and prints the larger number. If they are equal, print "Both numbers are equal".
num1=float(input("enter the value for number1: "))
num2=float(input("enter the value for number2: "))
if num1>num2:
    print("the larger number is: ",num1)
elif num2>num1:
    print("the larger number is: ",num2)
else :
    print("both are equal")

# 3.Write a Python program that asks the user for a number and prints whether it is positive, negative, or zero.
num=int(input("enter the number: "))
if num>0:
   print(num,"is positive number.")
elif num==0:
   print("it is zero.")
else :
   print(num,"is negative number.")

# 4.Write a program that asks the user for their age. If the age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote"
age=int(input("please entyer your age: "))
if age>=18:
    print("you are eligible to vote.")
else :
    print("you are not eligible to vote")


# 5.Write a program that takes a student's marks (out of 100) and prints:"Pass" if marks are 40 or more "Fail" if marks are less than 40
marks=int(input("enter student marks(out of 100): "))
if marks>=40 and marks<=100:
    print("Pass")
elif marks<40:
    print("Fail")
else:
    print("enter marks out of 100 only")
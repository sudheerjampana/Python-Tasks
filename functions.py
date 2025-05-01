# #functions

# def fruits():
#     print("apple","banana",)
# fruits()

# def tray1(*a):
#     print(a[1])
# tray1("apple","banana")

# def tray2(fruits):
#     print(fruits.append("guava"))
#     print(fruits)
# tray2(["apple","banana","grapes"])




# #1. write a function that takes two numbers as input and performs addition
# def add(x,y):
#     d=x+y
#     print("addition of two numbers is: ",d)
# add(4,6)

# #2.create a function that accepts a name and displays a personalized greeting
# def greetings(name):
#     print("hello","goodmorning",name)
# greetings("sudheer")

# #3. write a function to calculate the square of a given number
# def square(z):
#     e=z*z
#     print("square of a number is: ",e)
# square(33)

# #4.write a function to multiply two numbers
# def mul(a,b):
#     f=a*b
#     print("multiplication of two numbers is:",f)
# mul(2,3)

# #5. create a function that takes a string as input and prints the length of the string
# def text(greet):
#     i=len(greet)
#     print("length of the string is:",i)
# text("good morning every one")

# def div(a,b):
#     c=a/b
#     print("division of two values is:"+str(c))
# div(10,5)

# def sample(x,y,a=3,b=4):
#     print(x,y,a,b)
# sample(2,1)
# def sample(x,y,a=3,b=4):
#     print(x,y,a,b)
# sample(x=2,y=1)
# def sample(*,x,y,a=3,b=4):#here i mention keyword arguments by using(*,)
#     print(x,y,a,b)
# sample(x=2,y=1) #here i gives keyword arguments -->it gives op
# # def sample(x,y/,a=3,b=4): #here i mention positional 
# #     print(x,y,a,b)
# # sample(x=2,y=1) #here i got error but i give arguments as keword
# def sample(x,y,/,a=3,b=4): #here i mention positional by(/,)
#     print(x,y,a,b)
# sample(2,1) #arguments also in positional-->it gives op
# """finally i observes that 1.if we mention positional(/,) parameters then we have to give positional arguments
#                            2.if we mention keword(*,)parameters then we have to give keyword arguments
#                            3.in python takes both positional & keyword values 
#                            4.we have to mention(/,*,) for morev readability"""
# '''then'''
# def sample(x,y,/,*,a=3,b=4):
#     print(x,y,a,b)
# sample(2,1)


# def sample(x,y,name="sudheer",age=20):#in this 
#     print(x,y,name,age)
# sample(1,2)
# def sample(b,a):
#     print(a,b)
# sample(a=2,b=3)
# def tt(a=2,b=3):
#     print(a,b)
# tt()




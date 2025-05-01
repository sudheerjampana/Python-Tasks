# #Operators in python:
#  #these are used to perform an operation by using operands.
# #1.Arithmetical Operators-->[+,-,*,/,%,//,**]
# a=2  
# print(a+2) #here + Operator performs addition operation
# print(a-2) #here - Operator performs subtraction operation
# print(a*2) #here * Operator performs multiplication operation
# print(a/2) #here / Operator performs division operation by giving coefficient value as output
# print(a%2) #here % Operator performs Division operation by giving reminder as output
# print(a//2) #here // operator performs division operation by giving integer values as output
# print(a**2) #here ** operator performs exponential operation 
# #we take another type of example as
# a=10
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) 
# print(a//b) 
# print(a**b)

# #2.Assignment Operators-->[=,+=,-=,/=,%=,//=,**=]
# """this operators are used to make code simpler,faster, and more readable"""
# x=20 #here we takes x variable contains value 20 and i want add value 3 as shown below example
# """x=x+3 """#here we are adding 3 to x variable and storing result in x itself w/o using assignment operators
# x+=3 #here we are adding 3 by using assignment operator (both are same but this operators are used for simple and short code)
# print(x) #prints output as 23
# y=15
# y-=5 #here we taken assignment operator -=
# print(y)#it prints op as 10
# z=20
# #z**=5
# z//=5
# print(z)#it prints op as 100 
# #like was the all assignment operators works and these are helping to make code easier.


# #3.Logical Operators-->[and,or,not]
# #and operator gives true if both statements are true
# c=5
# print( c<10 and c>1)
# print(c<2 or c>1)
# print(not(c<2 or c>1)) #here true condition is given as input to not operation it gives output as false
# print(10 and 9)
# print(10 or 9)
# print(not(0)) #here not operator have single input only

# #4.Bitwise operators-->[&(and),|(or),~(not),^(xor),<<(Left Shift),>>(right shift)]
# print(True&True)
# print(True|False)
# print(1 ^ 0)

# print(~(-5)) # here NOT(~) symbol coverting all bits into one's complement(inverting all bits and adds+1)

# print(-10>>2)
# #5.Identity Operators--->[is, is not]

# #6.Comparision Operators-->[==,<,>,<=,>=,!=]
a=5
b=10
print(a==b)
print(a<=b)
print(b>=a)
print(a!=b)
# #7.Membership Operators--->[in, not in]
# book={"name":"novel",
#          "price":"90"}
# print("price" in book)
# bag1=["pens","pencils","books"]
# bag2=["slates","slate pencils",]
# print(bag1 not in bag2)
# print(id(bag1))
# print(id(bag2))
a={1,2,3}
b={1,2,3}
print(id(a))
print(id(b))
print(a==b)
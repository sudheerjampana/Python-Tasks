#Variables
a=2    #variables is used to store the data/values
print(a)   #OP:a=2

b=4
print(a+b)   #here we can reuse the variable 'a' to perform math operation OP:2+4=6

#in python variable names not contain any spaces b/w word to word. 
#to avoid this problem,to declare multiword variable names and to read easily by using following techinques

#1.Camel Case
myNameIs="sudheer" #in this case each word should be start with capital except first word
print(myNameIs)   #here myNameIs variable gives OP as sudheer
#2.Pascal Case
MyNameIs="sudheer" #in this case each word should be starts with capital only
print(MyNameIs)
#3.Snake case
My_Name_Is ="sudheer" #in this case each word has seperated with '_'(underscore)
print(My_Name_Is)

#note:python is a Case-sensitive language so we have to carefully assign variable names
#For Example
"""Age=20
print(AGE) #it shows error message that's why we have to careful with Caps Lock while using python"""
AGE=24
print(AGE) #here we get the Op as AGE=24





#Data Types
'''data type is nothing but type of data holds in variables'''
"""python mainly contains two types of data"""
#1.Primitive Data Types
'''primitive Data Types are immutable means it doesn't allow modifications after creating the variables'''
#integers(int) (it stores the whole numbers)
x=75  
print(type(x)) #here we can see type of data as 'int'

#float(float) (it stores the decimal values )
y=81.0
print(type(y)) #here we can see the type of data as 'float'

#String(str) (it stores group/ssequence of characters by declaring in "" or '' (double quotes or single quotes))
z= "sudheer"
print(type(z))  #here we can see the type of data as string

#Boolean(bool)
is_valid=True
print(type(is_valid)) #here we can see the type of data as boolean

#2.Non-Primitive Data Types
'''these data types are mutable means it can allows modifications after creating variables'''
#list (it represents ordered mutable collection of items)
c=[2,3,"hii","hello",True]
print(type(c)) #here we can see the type data as list
print(c)

#tuple (it represents ordered immutable collection of items )
d=(1,2,4,6,3)
print(type(d))  #here we can see the type of data as tuple
print(d)
#dictonaries(dict) (it represents prop[erties/key-value pairs)
novel={
    "name":"bookname",
    "pages":"90",
    "price":"50rs."}
print(type(novel))
print(novel)

#set (it represents unordered collection of unique values)
e={1,2,3,1}
print(type(e))
print(e)


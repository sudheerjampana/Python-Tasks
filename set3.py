# 1. Write a program to find the average of numbers in a list
num=[4,6,8]
count=0
sum=0
for i in num:
    count+=1
    sum+=i
print("average=",sum/count)

# 2. Write a program to count how many times a number appears in a list.
lst=[1,2,2,3,2]
num=2
count=0
for i in lst:
    if i==num:
        count+=1
print(count)

# 3. Write a program to get numbers greater than 5 from a list.
l=[2,5,7,8]
l2=[]
num=5
for i in l:
    if i>num:
        l2.append(i)
print(l2)

# 4. Write a program to replace all 0s with 1s in a list
inpt=[0,1,0,2]
rlst=[]
for i in inpt:
    if i==0:
        rlst.append(1)
    else:
        rlst.append(i)
print(rlst)

# 5. Write a program to print a list in reverse order
my_list=[1,2,3]
rev=[]
for i in my_list:
   rev=[i]+rev
print(rev)

# 6. Write a program to merge two dictionaries.
dct1={"a":1}
dct2={"b":2}
dct1.update(dct2)
print(dct1)

# 7. Write a program to create a dictionary from two lists (one for keys and one for values).
data={ }
data["a"]="1"
data["b"]="2"
print(data)

# 8. Write a program to print all values from a dictionary
this_dict={"x":5,"y":10}
x=this_dict.values()
print(x)

# 9. Write a program to get the length of a dictionary
inpt1={"a":10,"b":20,"c":30}
print(len(inpt1))

# 10. Write a program to list all items in a dictionary as tuples.
inpt2={"a":1,"b":2}
x=inpt2.items()
print(x)

# 11. Write a program to find the square of a number
num1=6
square=num1*num1
print(square)

# 12. Write a program to find the sum of digits of a number.
num2=123
sum=0
while num2!=0:
    digit=num2%10
    sum+=digit
    num2=num2//10
print(sum)

# 13. Write a program to find the smallest divisor of a number greater than 1.
n=15
divisors=[]
for i in range(1,n+1):
    if n%i==0:
        if i>1:
            divisors.append(i)
print(min(divisors))

# 14. Write a program to print the multiplication table of a number up to 10
number=3
for i in range(1,11):
    t=number*i
    print(number,"x",i,"=",t)

# 15. Write a program to count the number of even digits in a number.
s_inpt=2481
count=0
while s_inpt!=0:
    digit=s_inpt%10
    if digit%2==0:
        count+=1
    s_inpt=s_inpt//10
print(count)
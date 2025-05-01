# num=int(input("enter the num: "))
# count=0
# while num<=100:
#     print(num)
#     count=+1
#     num=num+1
#     print(count)

# num=5
# prime_not_found=True
# while prime_not_found:
#     num+=1 #6
#     fact=0
#     for i in range(1,num+1,1):
#         if num%i==0:
#            fact+=1
#     if fact==2:
#        prime_not_found=False
#        print(num,"is next prime")

"""upto here class"""

"""BY Using the While Loop"""
# Task 1 : Find the second prime of the given number ?
num=5
prime_count=0
while prime_count<2:
    num+=1
    fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact+=1
    if fact==2:
        prime_count+=1
print(num,"is second prime")

"""By using break control statement"""
# Task 2 : Break the loop if  Condition matches with the given number?
num=int(input("enter number (1-9 to break the loop): "))
for i in range(1,10,1):
    if num<=9:
        break
else:
    print("enter 1-9 only to break the loop ")

"""By using the continue control Sstatement"""
#  Task 3 : print the numbers from 1 to 100, but it should not print multiples of 3?
for i in range(1,101,1):
    if i%3==0:
        continue
    print(i,end=" ")


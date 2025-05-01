# e=[]
# o=[]
# for i in range(10,20):
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(e,o)

# p=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(p)):
#     if p[i]%2==0:
#         p[i]=p[i]*2
# print(p)

# p=[1,2,3,4,5,6,7,8,"python",True]
# for i in range(len(p)):
#     if type(p[i])==int and p[i]%2!=0:
#         p[i]=p[i]*2
# print(p)

# s=[1,10,20,30,50,60]
# sum=0
# for i in s:
#     sum+=i
# print(sum)

# string="python"
# rev=""
# for i in range(len(string)-1,-1,-1):
#     rev+=string[i]
# print(rev)
"""for i in range(-1,-7,-1):
    rev+=string[i]
print(rev)"""
# print(string[::-1])

# str1="sree"
# str2="sudheer"
# for i in range(len(str1)):
#     for j in range (len(str2)):
#         if str1[i]==str2[j]:
#             print(str1[i])

# import keyword as p
# print(p.kwlist)

# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1
# result += s[-1] + str(count)
# print(result)

# s = "abbccc"
# result = ""
# i=0
# while i<len(s):
#     count=1
#     while (i + 1) < len(s) and s[i] == s[i + 1]:
#         count += 1
#         i += 1
#     result += s[i] + str(count)
#     i += 1

# print(result)

# string="racecar"
# longest=""
# for i in range(len(string)):
#     temp=""
#     for j in range(i,len(string)):
#         if string[j] not in temp:
#             temp+=string[j]
#             print(temp)
#         else:
#             break
# if len(temp)>len(longest):
#     longest=temp
# print(longest)

# string="malayali"
# longest=""
# for i in range(len(string)): #0
#     temp="" #w
#     for j in range(i,len(string)):#01234 
#         temp+=string[j] #world
#         if temp==temp[::-1] and len(temp)>1: 
#             if longest=="" or len(temp)>len(longest):
#                 longest=temp
# if longest :
#     print(longest)
# else:
#     print("No palindromic Substrings")

# string="malayali"
# smallest="" #ala 
# for i in range(len(string)): #01234567
#     temp="" #malayali ala layal aya yal ali li i
#     for j in range(i,len(string)):#01234567 
#         temp+=string[j] #m ma mal mala malay malaya mayalal malayali
#         if temp==temp[::-1] and len(temp)>1:
#                 if smallest=="" or len(temp)<len(smallest):
#                     smallest=temp
#     #     print(temp)
#     # print(temp)
# if smallest :
#     print(smallest)
# else:
#     print("No palindromic Substrings")

# def length(l):
#     count=0
#     for i in range(len(l)):
#         count+=1
#     print(count)
# length()

# s="PyThOn DeVeLoPeR"
# res=""
# upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lower="abcdefghijklmnopqrstuvwxyz"
# for i in s:
#     if i in upper:
#         c_u=i.lower()
#         res+=c_u
#     elif i in lower:
#         c_l=i.upper()
#         res+=c_l
#     else:
#         res+=i
# print(res)

# s="python developer"
# # print(s[::-1])
# res=""
# # for i in range(len(s)-1,-1,-1):
# #     res+=s[i]
# for i in s:
#     res=i+res
# print(res)  


# s=[1,200,300,400,500,1000]
# a=s[0]#1 200 300
# # s.sort()
# # print(s[-1])
# for i in s:#1 200 300 400
#     if i>a: #1>1 200>1 300>200
#         a=i
#     print(a)
# print(a)

# s=[10,20,30,50]
# max1=0
# max2=0
# for i in s:
#     if i>max1:
#         max2=max1
#         max1=i
#     elif max1>i>max2:
#         max2=i
# print(max2)
# """patterns"""
# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         s+=str(i+1)+" "
#     print(s)

# n=5
# for i in range(1,n+1): #1 2 3 4 5
#     s=""
#     for j in range(i): #0 01 012 013 014
#         s+=str(i)+" "
#     print(s)

""""""""""""""""""""""""""
# n=5
# fact=0
# for i in range(1,n+1):
#     if n%i==0:
#         fact+=1
# if fact==2:
#     print(n,"is prime")
# else:
#     print(n, "is not prime")
# n=10
# for i in range(1,n+1):
#     if i>1:
#         prime=True
#         for j in range(2,i):
#             if i%j==0:
#                 prime=False
#                 break
#         if prime:
#             print(i)
"""next prime"""
# count=0
# while count<2:
#     n+=1
#     fact=0
#     for i  in range(1,n+1):
#         if n%i==0:
#             fact+=1
#     if fact==2:
#         count+=1
# print(n,"is next prime")

# 1. Print the list of prime numbers and non prime numbers separately in given list.
num_list=[1,2,3,4,5,6,7,8,9,10]
prime=[]
for i in range(len(num_list)):
    fact=0
    for j in range(1,num_list[i]+1):
        if num_list[i]%j==0:
            fact+=1
    if fact==2:
        prime.append(num_list[i])
print("prime list: ",prime)


# 2. Count the skills through the dictionary.
my_details={
    "name":"sudheer",
    "skills":["HTML","CSS","JS","Python"],
    "languages":["telugu","english","hindi"]
}
skills=my_details["skills"]
print(len(skills))





"""string palindrome"""
# s="madam"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)
# if rev==s:
#     print("palindrome")
# else:
#     print("not a palindrome")
"""model-1 of 1st largest number"""
# n=int(input())
# num=list(map(int,input().split()))
# largest=max(num)
# without_large=[]
# for i in num:
#     if i!=largest:
#         without_large.append(i)
# print(max(without_large))
"""model-2 of second largest number"""
# n = int(input())
# arr = list(map(int, input().split()))
# print(arr)
# unique = list(set(arr))
# print(unique)
# unique.sort()
# print(unique[-2])
"""Fibnocci values"""
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     next=a+b
#     a=b
#     b=next
"""Counting Vowels"""
# s="hello world"
# vowels="aeiouAEIOU"
# count=0
# for i in s:
#     if s[i] in vowels:
#         count+=1
# print(count)
"""Sum of integer"""
# num=123
# sum=0
# while num!=0:
#     last=num%10
#     sum+=last
#     num=num//10
# print(sum)
"""Frequency of char"""
# s=str(input())
# for i in s:
#     count=s.count(i
#         print(char,"is present",count)


# bal=input()
# int(bal)
# if bal.isnumeric:
#     if bal==0:
#         print("no funds")
#     elif bal>0:
#         print("bal is")
#     else:
#         print("dept")
# else:
#     print("invalid")
name="python developer"
rotation=1
start=97
end=122
res=""
for i in range(len(name)):
    char=name[i]
    code=ord(char)
    print(code)
    if code+rotation>122:
        rem=end-code
        extra=rotation-rem
        res+=chr(start+extra-1)
    else:
        res+=chr(code+rotation)
print(res)




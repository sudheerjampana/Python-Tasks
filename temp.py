# num=int(input("enter the number(contains 9 digits): "))
# count=0
# digit=int(input("enter the digit to check: "))
# positions=[ ]
# while num!=0:
#     last=num%10
#     positions.append(last)#2 7
#     if last==digit:
#         count=count+1
#     num=num//10
# positions.reverse()
# # print(positions)
# indices=[ ]
# for i in range(len(positions)):
#     if positions[i]==digit:
#        indices.append(i+1)
# if count>=1:
#     print(digit,"is present in the number")
#     print(digit,"is",count,"times present in the number")
#     print(digit,"occupies",indices,"position")
# else:
#     print(digit,"is not present in the number")

mt_list=list(input("enter values in list: "))
print(mt_list)
mt=tuple(input())
print(mt)
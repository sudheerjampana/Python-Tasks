# # 1.implement the count method on a list by taking input from the user without using the actual method.
# numbers=[2,4,5,7,9,9,10,12]
# num=int(input("enter the number to be counted: "))
# count=0
# for i in range(len(numbers)):
#     if numbers[i]==num:
#         count+=1
# print(count)

# # 2.implement the copy method on a list just as the above condition.      
# lst=[1,2,3,4,6,7,8]
# dup=[]
# for i in range(len(lst)):
#     if lst[i]<=len(lst)+1:
#         dup+=[lst[i]]
#         # dup.append(lst[i])
# dup.append(5)
# print(dup)

e_lst=[2,3,4,5,6,7,8,9]
primes=[]
non_primes=[]
for i in e_lst:
    if i>1:
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            primes.append(i)
        else:
            non_primes.append(i)
print("primes:",primes)
print("non primes:",non_primes)







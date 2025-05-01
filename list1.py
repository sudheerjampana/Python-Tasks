
"""List methods"""
# 1)Implement the program to print true when the first and last element in the list was even, else print false.
lst1=[2,3,4,5,6,7,9]
# last=len(lst1)
# print(last)
# if lst1[0]%2==0 and lst1[last-1]%2==0:
if lst1[0]%2==0 and lst1[len(lst1)-1]%2==0: #here we know that starting index of each list is 0

    print("True")
else:
    print("False")
# 2) implement the program to create a function which performs the count method. Without using any methods.
lst=[1,2,34,5,5,6,5]
ele=5
def count():
    count_val=0
    for i in range(len(lst)):
        if lst[i]==ele:
            count_val+=1
    print(count_val)
count()
# 3) write a program to print the prime numbers in the new list from the existing list.
e_lst=[2,3,4,5,6,7,8,9]
n_lst=[]
for i in e_lst:
    if i>1:
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            n_lst.append(i)
print(n_lst)

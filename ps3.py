lst=[1,2,4,3,5,2,1]
temp=[]
for i in lst:
    if i not in temp:
        temp.append(i)
print(temp)
count=len(lst)-len(temp)
for i in range(count):
    temp.append(("*"))
print(temp)
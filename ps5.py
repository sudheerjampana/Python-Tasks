rows=int(input("enter the number of rows: "))
count=97
for i in range(1,rows+1):
    res=''
    for j in range(1,i+1):
        if i==j or i==rows or j==1:
            res+=chr(count)+" "
        else:
            res+=" "+" "
        count+=1
    print(res)
rows=5
mid=rows//2
for i in range(rows):
    res=""
    for j in range(rows):
        if i==0 or i==rows-1 or j==mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
for i in range(rows):
    res=""
    for j in range(rows):
        if j==0 or i==rows-1:
            res+="*"+" "
    print(res)
for i in range(rows):
    res=""
    for j in range(rows):
        if j==0 or  i==mid or i==0 or (i==1 and j==rows-1) :
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
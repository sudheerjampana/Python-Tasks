num=957362172
temp=num
length=0
digit=2
positions=[ ]
while num!=0:
    num=num%10
    length+=1
    if num==digit:
        print(digit,"is present in this number")
        while temp!=0:
            pos=temp%10
            positions.append(pos)
            temp=temp//10
        # print(positions)
        positions.reverse()
        print(positions.count(digit))
        indices=[ ]
        for i in range(len(positions)):
            if positions[i]==digit:
                indices.append(i+1)
        print(indices)

        # indices = [i for i, val in enumerate(positions) if val == digit]  #i researched in google to print multiple indices
        
    else:
        print(digit,"is not present in this number")
    num=num//10
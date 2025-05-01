num=9603947547
count=0
myl=[ ]
while num!=0: #it iterates until condition got false
    last=num%10 #3 #2 #1 are iterating
    fact=0
    for i in range(1,last+1): 
        if last%i==0:
            fact=fact+1
    if fact==2:
        myl.append(last)
        # print(last,"is prime digit")
        count+=last
    # else:
    #     print(last,"is non-prime digit")
    num=num//10
print("there is",len(myl),"prime digits in the number")
print(myl,"are the primes digits in the number ")
print("total count of the number is",count)


    


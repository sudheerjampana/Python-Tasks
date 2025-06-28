# Task1 Print the prime digits in the given number
num=123475
primes=[]
while num!=0:
    last=num%10
    if last>1:
        fact=0
        for i in range(2,last):
            if last%i==0:
                fact+=1    
        if fact==0:
            primes.append(last)
    num=num//10
print(primes)


# Task2: Practice Armstrong number program
n=153
temp=n
length=0
while n!=0:
    n=n//10
    length+=1
# print(length)
temp2=temp
total=0
while temp!=0:
    last=temp%10
    total= total+(last**length)
    temp=temp//10

if total==temp2:
    print("armstrong")
else:
    print("Not armstrong")
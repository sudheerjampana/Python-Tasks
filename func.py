# sudheer=lambda x,y,z:x+y+z
# print(sudheer(1,2,3))


# n1=int(input("enter number1: ")) #4
# n2=int(input("enter numbe2: "))#2
# maximum=max(n1,n2)#4
# count=0
# prime=2
# while count<=maximum: #0<4
#     fact=0
#     for i in range(2,prime): #2
#         if prime%i==0: #2 
#             fact+=1
#             break
#     if fact==0:
#         count+=1
#         if count==n1 or count==n2:
#             print(prime)
#     prime+=1

 
# def to_find_large():
#     maximum=max(n1,n2)
#     return maximum
# def take_prime():
#     count=0
#     mul=1
#     p=2  
#     while to_find_large()>=count:
#         fact=0
#         for i in range(2,p):
#             if p%i==0:
#                 fact+=1
#                 break
#         if fact==0:
#             count+=1
#             if count==n1 or count==n2:
#                 print(p)
#                 mul=mul*p
#         p+=1
#     print(mul-1)
# n1=int(input("enter number1: "))
# n2=int(input("enter number2: "))
# # print(prime())
# print(take_prime())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes(n1, n2):
    maximum = max(n1, n2)  # Find the maximum of the two numbers
    count = 0
    prime =0
    mul=1
    
    while count <= maximum:
        if is_prime(prime):
            count += 1
            if count == n1 or count == n2:
                print(prime)
                mul=mul*prime
        
        prime += 1
    print(mul-1)
# Function calls
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
find_primes(n1, n2)
  
# for i in range(1,101,1):
#     if i%3==0 and i%5==0:
#         print("fizz buzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# n=4
# count=97
# for i in range(n):
#     res=""
#     for j in range(i+1):
#         res+=chr(count)+" "
#         count+=1
#     print(res)
# rows=5
# count=97
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,i+1):
#         if i==j or i==rows or j==1:
#             res+=chr(count)+" "
#         else:
#             res+=" "+" "
#         count+=1
#     print(res)

"""
1
2 3
4 5 6
7 8 9 10

* * * * *
*       *
*       *
*       *
* * * * *

a
b c
d e f
g h i j 
k l m n o

*
* *
*   *
*     *
* * * * *

X O X O X
O X O X O
X O X O X
O X O X O
X O X O X
"""
# rows=4
# count=1
# for i in range(rows):
#     s=""
#     for j in range(i+1):
#         s+=str(count)+" "
#         count+=1
        
#     print(s)

rows=5
for i in range(rows):
    s=""
    for j in range(rows):
        if i==0 or j==0 or i==rows-1 or j==rows-1:
            s+="*"+" "
        else:
            s+=" "+" "
    print(s)


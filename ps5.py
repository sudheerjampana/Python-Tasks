"""a 
b c
d   f
g     j
k l m n o
"""
# rows=int(input("enter the number of rows: "))
# count=97
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,i+1):
#         if i==j or i==rows or j==1:
#             res+=chr(count)+" "
#         else:
#             res+=" "+" "
#         count+=1
#     print(res)
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
# rows=5
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i+j>=rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)
"""
*
* *
* * *
* * * *
* * * * *
"""

# rows=5
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i+j<=rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

"""
* * * * * * * 
*           * 
*           *
*     *     *
*           *
*           *
* * * * * * *
"""

# rows=9
# center=rows//2
# for i in range(rows):
#     s=""
#     for j in range(rows):
#         if i==0 or j==0 or i==rows-1 or j==rows-1 or i==j==center:
#             s+="*"+" "
#         else:
#             s+=" "+" "
#     print(s)


# rows=5
# mid=rows//2 + 1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows or i==mid and j==mid:
#            res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# rows=5
# mid=rows//2 + 1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows:
#            res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

"""
*       *
 *     *
  *   * 
   * *
    *
"""
rows=5
for i in range(rows,0,-1): # 5 4 3 2 1
    res=""
    for sp in range(rows-i): #5-1=4=>
        res+=" "
    for j in range(i):
        res+="*"+" "
    print(res)
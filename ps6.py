"""
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
"""
# rows=5
# for i in range(rows,0,-1):
#     res=""
#     for j in range(i,0,-1):
#         res+=str(i)+" "
#     print(res)

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
# rows=5
# for i in range(1,rows+1): # 1 2 3 4 5
#     res=""
#     for sp in range(rows-i): #5-1=4=>
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

"""
* * * * *
 * * * * 
  * * *
   * *
    *
"""
# rows=5
# for i in range(rows,0,-1): # 5 4 3 2 1
#     res=""
#     for sp in range(rows-i): #5-1=4=>
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)

"""
*       *
*       *
* * * * *
*       *
*       *
"""
rows=5
mid=rows//2
for i in range(rows):
    res=""
    for j in range(rows):
        if j==0 or  i==mid or j==rows-1 :
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

        
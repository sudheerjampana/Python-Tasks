# Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not 
# and also check the citizen.if both conditions are True add { eligible: True}
voters_list=[{'name':'sudheer','age':21,'citizen':'indian'},
             {'name':'pandu','age':21,'citizen':'indian'},
             {'name':'alice','age':20,'citizen':'american'}]

for  i in voters_list:
    if i['age']>18 and i['citizen']=='indian':
        i['eligible']=True
    else:
        i['eligible']=False
print(voters_list)

# Take a tuple of elements, print the unique elements in the new list

s=(1,2,3,4,4,5,6,1,7,8,3,9)
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(l)

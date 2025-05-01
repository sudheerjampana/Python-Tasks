# string=input("enter the string to be rotated: ")
# rotations=int(input("enter rotations: "))
# # string=[1,2,3,4,5,6]
# rotations=rotations%len(string)

# for i in range(rotations):
#     string=string[1:len(string)]+string[0:1]
# print(string)
"""like Coding decoding 27th letter is a"""
rotations=1
name="python developer"
result=""
start=97
end=122
for i in range(len(name)):
    char=ord(name[i])
    # print(char)
    char=char+rotations
    if char>122:
        extra=char-end 
        char=start+extra-1
        # print(chr(char))
        result+=chr(char)
    elif char<97 and char>72: #if we not mention char>72 then the special characters values also taken here
         req=start-char
         letter=end-req+1
        # print(chr(letter))
         result+=chr(letter)
    else:
        result+=chr(char)
print(result)
"""Like Coding Decoding in Reverse order"""
# rotations=-1
# name="sudheer"
# st=97
# ls=122
# res=""
# for i in range(len(name)):
#     asc=ord(name[i])
#     val=asc+rotations
#     if val<97:
#         req=st-val
#         letter=ls-req+1
#         # print(chr(letter))
#         res+=chr(letter)
#     else:
#         res+=chr(val)
# print(res)
    # print(chr(val))

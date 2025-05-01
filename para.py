string=str(input("enter the paragraph: "))
for i in string:
    # print(i)
    if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)) or (ord(i)==32) :
        valid=True
    else:
        valid=False
        break
if valid:
    print("valid the paragraph contains alphabets and spaces only")
else:
    print("invalid!! the paragraph contains special characters also")

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
space=" "
valid=True
for i in string:
    if not i in upper and not i in lower and not i in space:
        valid=False
        break #here break stops the iteration if any one char fails the condition 
if valid:
    print("valid")
else:
    print("invalid")


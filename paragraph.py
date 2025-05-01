#Task 1: Take  a paragraph check the count of words, if count is more than 100, print valid ; else invalid
para=input("enter the 6 lines of paragraph seperated by space : ") #taking input from the user
new=para.split(" ") #splitting the words into new variable
# print(new)
for i in range(len(new)): #to iterating the total words using len
      print(i+1,new[i]) #to print number and word
print("the paragraph contains",len(new),"words") 
if len(new)>=100: #checking wether the paragraph containing 100 words 
    print("valid") #if the para contains 100 words it will prints valid
else:
    print("invalid") #if the para doesn't contains 100 words it will prints invalid


# Task2: take a input with both upper and lower cases characters count the no.of  uppercases and lower cases without using any methods
word="SuDhEeR"
ucount=0
lcount=0
for i in range(len(word)):
    if ord(word[i])>=61 and ord(word[i])<=90:
        ucount+=1
    else:
        lcount+=1
print("there is ",ucount,"Upper case Letters in that string")
print("there is ",lcount,"lower case Letters in that string")

"""python follows pass/call by object reference"""
'''pass by values -->when these are immutable'''
'''pass by reference-->when these are mutable'''
def example(a,b=3,c=5):
    print(b,a,c)
example(1,2,3) #here it overwrites the value because its passes by value

def example1(a,b="hii",c=5):
    print(a,b,c)
example1("sudheer",2,3) #here also passes by value itself 
# finally immutables like int,str,tuple passes by values 
def example2(x):
    x=[1,2,3]
    print(x)
    z=[3,4,5]
example2()#here its passes by reference(object which is' x 'in parameters) and overwrites arguments
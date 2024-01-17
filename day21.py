#function
#progarm1

def add (x,y):
    return x +y
q1=add(14,5)
print(q1)

def sub (x,y):
    return x -y
q2 = sub(41,6)
print(q2)

#program2
add = lambda x,y:x+y
q3=add(41,5)
print(q3)

#progarm3

squ = lambda x:x*x
q= squ(5)
print(q)

#program 4

def additionall(*args):
    (args)
    total = 0
    for i in args:
        total = total +i
        return total
a=additionall(114,2,5,5,66,3,366,94,45,588,55)
print(a)

#progeram 5

def addcity(**kwargs):
    print(kwargs)
    kwargs["city"]="mumbai"
    return kwargs
a2=addcity(fullname = "snehal",city="nagpur",age=22)
print(a2)


#program 6

def addition(x=4,y=6):
    print(x+y)
addition()
addition(14,5)

def sub(y=21,z=45):
    print(y-z)
sub()
sub(41,5)

#program 7
def addition(x1,x2,x3):
     print(x1+x2+x3)
     print(x3)
addition(14,45,8)
addition(x1=4,x2=55,x3=6)
print(x2)


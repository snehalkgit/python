##lmabda function

def add(x,y):
    return x + y
a= add(55,5)
print(a)


add = lambda x,y :x+y
b= add(12,6)
print(b)


# program 2
e = lambda x:x*x
print(e(16))


##lambda function

##program 3
def addition(x,y):
    return x +y
print(addition(12,88))


##program 4

# function as parameter to another function

add= lambda x , y : x +y
def addition(fn,x,y):
    f=fn(x,y)
    return f
s2= addition(add,14,66)
print(s2)

##program 5

# program 4
# function as a return type
def add():
    return lambda x,y :x+y
e = add()
print(e)
s2 = e(12,3)
print(s2)







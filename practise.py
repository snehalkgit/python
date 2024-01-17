
#function without parameter and with return type

def add():
    print(8+4)
add()

def sub():
    print(54-98)
sub()

def mul():
    print(4*5)
mul()

### function with parameter and without return type

def addA(a,b):
    print(a+b)
addA(45,5)

def subA(x,y):
     print(x-y)
subA(45,8)


#function with parameter  and with return type

def addA(a,b):
    return a +b
addA(14,5)
a1 = addA(24,6)
print(a1*5)


def subB(p,q):
    return p - q
q= subB(14,6)
print((q-5))

##list...

number = [14,56,78,55,25,23,11,44]
print(number)
print(type(number))
for x in range(len(number)):
 print(x)


number.append(45)
print(number)
for x in number:
    print(x)
    print(type(x))

for item in number:
    print(item)

## strings in list
names=["snehal","sarang","shubham","dipika","manisha"]
print(names)
print(type(names))
print(names[2])
print(names[0])
names.append("saru")
print(names)
print(names.pop())
print(names.count("snehal"))

number2=[14,5,4,5,6,2,22,545,45,6,222,445,88,44,556,222,55,22,44,55]
print(number2.count(22))
print(number2.pop())
print(number2.index(5))
print(number2)

#list strore duplicate values but not in set

##mixedarray

array=["snehal",251544,True,False]
print(array)
print(type(array))  #-====list

print(array.pop())

#list  of cities

cities=["mumbai","goa","nagpur","hydrabad","bhopal"]
print(cities)
print(type(cities))

#on list we can add , retrive,update,delete

#retrive
print(cities)
#update
cities[0]="hinganghat"
print(cities)
#add
cities.append("nandori")
print(cities)
#delete
cities.pop()
print(cities)

cities.remove("goa")
print(cities)




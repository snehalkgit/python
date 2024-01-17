#tuple

listA=[22,33,55,44,55]
print(listA)
print(type(listA))

s = (5,4,5,2,5,5)
print(s)
print(type(s))

s1 = 1,5,7,4,5,8
print(s1)
print(type(s1))

#why tuple
names = ["snehal","sarika","shubham","nikita"]
names.append("samikha")
print(names)

names[0]="sami"
print(names)

cities=("pune","mumbai","goa","hyd")
print(cities)
#can we acess tuple by cities
print(cities[0])




# using range() function
for x in range(len(cities)):
    print(x)
    print(cities[x])

# without range()
fruits = "apple","mango","banana"
for item in fruits:
    print(item)

#fruits[0] = "banana"
fruits = ("apple","mango","grapes","mango")
print(len(fruits))

# del fruits
# print(fruits)

animals = ('panda',"lion","rabbit","tiger")
# x = animals[0]
# y = animals[1]
# z = animals[2]

x,y,z,A = animals
print(x)
print(y)
print(z)
print(A)

c1 = animals.count("tiger")
print(c1)

q1 = animals.index("panda")
print(q1)



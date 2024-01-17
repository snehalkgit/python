names = ["snehal","rahul","shubham"]
##retrive
print(names[0])

##add

names.append("salon")
print(names)

##update
names[0]="laxmi"
print(names)

##delete

names.pop()
print(names)


cities=["pune","mumbai","goa","banglore"]
print(cities)

print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])


 #for loop using range

for x in range(len(cities)):
    print(x)
    print(cities[x])

#program 2
countries= ["india","srilanaka","pakistan","japan","china"],
for x in range(len(countries)):
    print(countries[x])


#program 3

fruits = [ "mango", "banana","apple","kiwi"]
for a in fruits :
    print(a)

#program 4

a = 10
print(a)

b = 100
print(b)
b = 150
print(b)
print(a)

listA = [11,55,88]
print(listA)

listB = listA
print(listB)
print(listA)

listB[0]=55
print(listA)

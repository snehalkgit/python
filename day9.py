names = ["samiksha","snehal","kajal","saloni"]
print(names)
print(names[2])
namesB = names
print(namesB)

names[1]= "sarika"
print(names)


#remove
cities= ["mumbai","goa","nagpur","indore","kolkata"]
cities.remove("goa")
print(cities)


#pop()
cities2= ["mumbai","goa","nagpur","indore","kolkata"]
cities2 .pop(1)
print(cities2)


#claer(
#cities2.clear()
#print(cities2)

fruits = ["apple","mango","'papaya","apple","grapes","apple"]
q1=fruits.index("apple",1,5)
q2= fruits.index("apple")
print(q1)
print(q2)

#reverse
cities= ["goa","nagpur","wardha","chennai","pune"]
cities.reverse()
print(cities)


#sort()
cities.sort()
print(cities)

#append()
country=["india","banagaladesh","srilnka","cuba"]
country.append("china")
print(country)

#insert
country.insert(2,"china")
print(country)


#extend()
numberA=[1,5,6]
numberB=[5,4,8,6]

numberA.extend(numberB)
print(numberA)
print(numberB)

#count
flowers =["lily","rose","jasmin","zendu","jasmin", "sunflower"]
flowers.count("jasmin")
print(flowers)

i =[14,55,66]
s=i.copy()
i[0]=555
print(i)



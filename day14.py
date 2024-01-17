listA=["snehal","shubham","sarika","kirti"]
##retrive

print([listA[0]])
print(listA)

##update

listA[0]="samiksha"
print(listA)

##ADD

listA.append("pune")
print(listA)

##delet
del listA

#total number of elemenet


listA=["snehal","samiksha","purva","purva"]
for item in listA:
    print(listA)

for item in range(len(listA)):
   print(listA)

 #dictonary

info = {
     "firstname ":"snehal",
     "lastname ":"kamble",
    "age":24,

}

#dict does not stores the value by index

a1= info["firstname "]
print(a1)

#update
info["lastname "]="gedam"
print(info)

#add
info['city']="mumbai"
print(info)

#dele
del info


#check whether elements is present #looping through list

cities=["goa","mumbai","hydrabad","pune"]

for item in cities:
    print(item)


#present or  not gives true or false
print("wardha"in cities)
info2 = {
    "firstName":"snehal",
    "lastName":"kamble",
    "age":24
}
print("age" in info2)
for item in info2:
    #print(item)
    print(item ,info2[item])


car = {
    "color":"white",
    "model":"xz",
    "company":"altroz"
}

for item in car:
    print(item,car[item])

#get()
q3 = car.get("model")


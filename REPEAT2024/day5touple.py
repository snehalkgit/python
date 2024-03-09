##touple vs list


# list = ["snehal","sayli","samiksha","laxmi"] ##list
#
# print(list)
# print(type(list))
#
# list.append("sami")
# print(list)

str= "snehal"  ##string
print(str)
print(type(str))

info={
    "firstname":"snehal",
    "lastname":"kamble"
 }

print(info)
print(type(info)) ##dict


## program 2

flowers=["rose","lily","sunflower","lotus"] ##list
flowersA=("lily","lotus","rose")  ##touple

print(flowers)
print(type(flowers))  ##list

print(flowersA)
print(type(flowersA)) ##touple


#does  tuple stores the value by index??
# how to define tuple

tuple=["A","B","C","D"]  ##list
print(tuple)
print(type(tuple))

print(tuple[1])
print(tuple[2])
print(tuple[3])

for x in range(len(tuple)):
    print(x)

##without range

for item in tuple:
     print(item)


##while

i = 0
while(i<len(tuple)):
    print(tuple[i])
    i = i + 1


##program 3

numbers=12,54
print(numbers)
print(type(numbers)) ##tuple

##we cant add number to touple but we can add in list .. we can convert tuple in list n then  add to it


tupleB=(84,11,44,56,22,55,45,48)
print(tupleB)
print(type(tupleB))
print(len(tupleB))

a=list(tupleB)
print(a)
a.append(45)
print(a)




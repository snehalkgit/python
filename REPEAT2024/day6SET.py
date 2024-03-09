##program1
names = ["snehal","kamble","sayli","laxmi"]
print(names)
print(type(names)) ##list

##program2

info={
    "firstname":"snehal",
    "lastname":'kamble',
    "rollno":5,
    "age":25
}
print(info)
print(type(info)) ##dict

##program 3

##SET

number={45,65,1,2,56,36,5,56}
print(number)
print(type(number)) ##set

##set does not allow duplicate value

number2={45,65,1,44,55,66,55,2,56,36,5,56}
print(number2)
number2.add(44)  ##addd
print(number2)


##pop
##remove random number

number2.pop()
print(number2)

##remove

##remove can remove only number we have passed

number2.remove(55)
print(number2)


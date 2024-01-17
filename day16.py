dict ={
    "firstname" :"snehal",
    "lastname":"kamble",
    "age":24,
    "email":"snehalkamble1564@gmail.com"
}
dict2= dict
dict2['rollno']=25
print(dict)
print(dict2)

dict3={
    "firstname":"snehal",
    "lastname":"kamble",

}

#program1
#copy()
dict4=dict3.copy()
dict4["lastname"]="gedam"
print(dict4)
print(dict3)

#program2

#update()
info={
    "color":"black",
    "model":"xz"
}
info2={
    "regno":1245
}

info2.update(info)
print(info)
print(info2)

#program3  pop item
info={
    "color":"white",
    "mobileno":145,
    "city":"mumbai"

}
info.popitem()
print(info)

#prpogram4
#setdeafault()

info={
    "city": 457,
    "disrtict":45,
    "state":25

}
info.setdefault("city",245)
print(info)

# program 5
props = ["fn","ln","age"]
info5 = dict.fromkeys(props,0)
print(info5)

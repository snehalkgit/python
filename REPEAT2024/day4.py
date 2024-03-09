# ##program1
#
# #upper()
#
# first_name = "snehal"
# print(first_name.upper())
# print(len(first_name))
#
#
# ##lower
#
# last_name = "KAMBLE"
# print(last_name.lower())
#
#
# middle_name = "kawadu"
# print(middle_name.isupper())
#
# e2= last_name="KAWADU"
# print(e2.isupper())
#
# print(middle_name.islower())
#
#
# ##lower(), upper(),isupper(),islower()
#
# city = "mumbai"
# print(city.startswith('m'))
# print(city.startswith('M'))
# ##we can use substring also
#
# city2 = "hydrabad"
# print(city2.endswith('d'))
# print(city2.endswith('bad'))
#
#
# city3= "nagpurr"
# print(city3.count('a'))
# print(city3.count('r'))
#
#
# ##lstrip method ahe rstrip metho
#
# city4=("  wardha")
# print(len(city4))
# c1=city3.lstrip()
# print(c1)
# print(len(city4))
#
#
# city3=("  wardha  ")
# c2=city3.rsplit()
# print(c2)
# print(len(city3))
#
# e3=city3.strip()
# print(e3)
#
# # program 4
# info = "I am learning sql"
# e4 = info.replace("javascript","python")
# print(e4)
# print(info)
#
#
# # program 5
# e14 = "12321323".isdigit() #  0 to 9
# print(e14)
#
# e15 = "123545and#"
# e16 = e15.isalpha()
# print(e16)
#
# e17 = e15.isalnum()
# print(e17)
#
# e6="abdsjnsj"
# print(e6.isalpha())
#
#
# ##program6
#
# first_name = "snehal"
# print(first_name.startswith('s'))
# print(first_name.startswith('sne'))
# print(first_name.startswith('al'))
#
#
# ##program 7
# last_name = "kamble"
# print(last_name.endswith('e'))
# print(last_name.endswith('le'))
# print(last_name.endswith('Ble'))

##program 8

full_name = " kamble"
e3 = full_name.isspace()
print(e3)

full_name="kamble "
e2= full_name.isspace()
print(e3)


##program 9
name = "snehal"
##print(name.capitalize())
e5=name.capitalize()
print(e5)

##program 10

e1="I AM  learning javascript"
print(e1.istitle())

e6="I Am Larning Js"
print(e6.istitle())

##program 11

info=["snehal","kamble"]
s1=" ".join(info)
print(s1)

s2="--".join(info)
print(s2)

info2="snehalkamble@gmail.com"
e3=info2.split('@')
print(e3)


##program 12

##find
fullname="snehalkamble"
print(fullname.find('a'))
print(fullname.find('a',5))

##removeprefix

email2 = "gmail.com@snehal"
email3 = "gmail.com@sayli"
email4 = "gmail.com@sam"

#print(email4.removeprefix('gmail.com@'))
# ["snehal","sayli","sam"]
students = [email2,email3,email4]
list = []
for x in students:
  q1 = x.removeprefix("gmail.com@")
  list.append(q1)
print(list)


##removesuffix

students = {
    "1":"snehalceo",
    "2":"poorvaadmin",
    "3":"shamcustomer",
    "4":"nirnaymanager"
}

roles = ["ceo","admin","customer","manager"]
names = []
#names =["snehal","poorva","sham","nirnay"]
for name in students.values():
  for role in roles:
    if role in name:
      q2 = name.removesuffix(role)
      names.append(q2)
print(names)

#swapcase()
a = "hellooo"
print(a.swapcase()) ##caplital


#zfill()
name = "snehal"
name2 = "sayli"

print(name2.zfill(10))
print(name.zfill(4))






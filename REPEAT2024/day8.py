##inti as parameter and inti as return type

def add(x,y):
    return x+y
a= add(12,5)
print(a)


##float as parameter and float as return type


def sub(x,y):
  return x -y
A= sub(25,66)
print(A)

##bollean as parameter and return type

def candrive(age,havevehicle):
    if age > 18 and havevehicle:
        return True

    else:
        return False

B= candrive(19,True)
print(B)

 ##string as parameter and string as return type

def greet(name):
     return("welcome"+name)
S = greet("snehal  !")
print(S)


##list as parameter and list as return type

name = ["chaitan","snehal","chinmay","sayli"]
def addName(lst):
    lst.append("sonu")
    return lst
a= addName(name)
print(a)
# dictionary as parameter and dictionary as return type
info = {
    "firstName":"snehal",
    "lastName":"kamble"
    #city:hinganghat
}
def addCity(information):
    information['city'] = "hinganghat"
    return information
city= addCity(info)
print(city)

# tuple as parameter and tuple as return type
numbers = (11,22,33,55,75,66)
def addValue(tupA):
    #(11,22,33)
    tupA = list(tupA)  # [11,22,33]
    tupA.append(8)  #[11,22,33,44]
    tupA = tuple(tupA) #(11,22,33,44)
    return tupA
N= addValue(numbers)
print(N)

# set as parameter and set as return type
setA = {11,22,33}
def addElement(seta):
    seta.add(44)
    return seta
z = addElement(setA)
print(z)

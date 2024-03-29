class Person:

    # fields or properties
    first_name = "snehal"
    last_name = "kamble"

    # instance
    def walk(self):
        print("I am walking")

    def talk(self):
        print("I am talking")

snehal = Person()
print(snehal.first_name)
print(snehal.last_name)
snehal.walk()
snehal.talk()

niki = Person()
print(niki.first_name)
print(niki.last_name)
niki.walk()
niki.talk()

niki.first_name = "nikita"
niki.last_name = "kamble"

print(niki.first_name)
print(niki.last_name)


##program 2
class PersonB:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def talk(self):
        print("I am talking")

    def walk(self):
        print("I am walking")


surya = PersonB("surya", "yadav")
sachin = PersonB("sachin", "kamble")

print(surya.first_name)
print(surya.last_name)

print(sachin.first_name)
print(sachin.last_name)
sachin.city = "pune"
print(sachin.city)
sachin.city = "mumbai"
print(sachin.city)

# Assignment
# Vehicle
# type model
# start() , stop()


class Vehicle:
    def __init__(self,ty,md):
       self.type = ty
       self.model = md

    def start(self):
        print("car is start")

    def stop(self):
        print("car is stop")

snehal = Vehicle("tata","altroz")

print(snehal.model)
print(snehal.type)
print(snehal.stop())
print(snehal.start())



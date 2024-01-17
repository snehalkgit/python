# Program 1
class Person:
    firstName = None
    lastName = None
    age = None
    rollNo = None
    def displayName(self):
        print(self.firstName + self.lastName)

snehal = Person()
print(snehal.firstName)
print(snehal.lastName)
print(snehal.age)
print(snehal.rollNo)
#amol.displayName()

snehal.firstName = "snehal"
snehal.lastName = "kamble"
snehal.age = 23
snehal.rollNo = 45

print(snehal.firstName)
print(snehal.lastName)
print(snehal.age)
print(snehal.rollNo)
snehal.displayName()

# program 2
class PersonB:
    def __init__(self,fn,ln,ag,roll):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.rollNo = roll

    def displayName(self):
        print(self.firstName  + self.lastName)

saru = PersonB("saru","kadu",34,66)
kawadu= PersonB("kawadu","kamble",55,44)
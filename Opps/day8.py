##program1

class Employee:
    def __init__(self,fn,ln,adharno):
        #instance properties
        self.firstname = fn
        self.lastname = ln
        self.adhar = adharno

        #instance method
    def displayName(self):
     print(self.firstname+self.lastname)

    def changeadhar(self,change):
         self.addhrno = change


x = Employee("snehal","kmable",1225463231)

print(x.firstname)
print(x.lastname)
print(x.adhar)



##program2

class Employee:
    country = "india"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    @classmethod
    def changecountry(cls):
     cls.country = "bharat"

    def displayname(self):
        print(self.firstname + self.lastname)

y = Employee("nikita","kamble")
print(y.firstname)
print(y.lastname)
y.displayname()

snehal = Employee("snehal","kamble")
print(snehal.lastname)
print(snehal.firstname)

Employee.changecountry()
print(snehal.country)
print(y.country)
snehal.country = "thailand"
print(snehal.country)


##number of object

class Myclass:
    n = 15
    def __inti__(self):
        Myclass.n = Myclass.n +1

    @staticmethod

    def noofobject():
            print(Myclass.n)

object1 =Myclass()
object2=Myclass()

Myclass.noofobject()



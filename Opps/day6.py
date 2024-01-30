##Abstract class

class Myclass:
    def calculator(self,x):
        print(x)

obj= Myclass()
obj.calculator(1)
obj = Myclass()
obj.calculator(25)
obj = Myclass()
obj.calculator(23)

#cube

#square
#squareroot


from abc import ABC,abstractmethod

class myclass(ABC):
    @abstractmethod
    def calculate(self):
        pass

class square(myclass):
    def calculate(self,x):
        print("square")
class cube(myclass):
    def calculate(self,y):
        print("cube")

class squareroot(myclass):
    def calculate(self,z):
        print("squareroot")


# we cannot create object of abstract class
# abstract class can have - abstract method and non - abstract method
# it mandatory for class to implement abstract method if inherited


print(squareroot)
print(cube)
print(myclass)

##program2

class vehicle(ABC):
    @abstractmethod
    def wheel(self,x):
        pass
    def country(self):
        print("india")

class Tata(vehicle):
    def wheel(self,x):
        print("4 wheels")

class truck(vehicle):
    def wheel(self,x):
        print("8 wheels")

s=Tata()
s.wheel(5)
s.country()

b= truck()
b.wheel(8)
b.country()


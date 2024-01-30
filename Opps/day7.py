##program1

class calculator:
    #class level variable
    c = 10
    def __init__(self,x,y,z):
         #instance variabl
         self.x = x
         self.y = y
         self.z = z
A = calculator(154,2,36)
print(A.x)
print(A.y)
print(A.z)


##program2

#changing value of instance level variables
class calculator:
    x = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

        #instnace level method
    def changex(self,chnage):
            self.x = chnage

snehalA = calculator(14,5)
print(snehalA.x)
print(snehalA.y)

class calculatorA:
    a = 15
    def __init__(self,x,y):
        self.x = x
        self.y = y
        @classmethod
        def chnageA(cls,ch):
          cls.c = ch

saru = calculatorA(1,5)
print(saru.x)
print(saru.y)
print(saru.a)

snehal = calculatorA(42,5)
print(snehal.x)
print(snehal.y)
print(snehal.a)











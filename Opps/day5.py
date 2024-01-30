#polymorphism

#Duck typing
class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hello snehal")
class Dog:
    def talk(self):
        print("bow bow")
def call_talk(obj):
    obj.talk()

A = Dog()
B = Human()
C = Duck()

call_talk(A)
call_talk(B)
call_talk(C)

##program 2

class Duck:
 def talk(self):
     print("quack quack")

class Human:
    def talk(self):
        print("hiii")


class Dog:
    def talk(self):
        print("bow bow")

class Cat:
    def sound(self):
        print("meow meow")


def call_talk_sound(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'sound'):
           obj.sound()

a = Dog()
b = Human()
c = Duck()
d = Cat()

call_talk_sound(a)
call_talk_sound(b)
call_talk_sound(c)
call_talk_sound(d)


##operator overloading

print((1+1+2))
print("1"+"hii")

class BOOKX:
    def __init__(self,x):
        self.pages = x
    def __add__(self,other):
        return self.pages + other.pages

class BOOKY:
    def __init__(self,y):
        self.pages = y


harrypotter = BOOKX(100)
geeta = BOOKY(2000)
print(harrypotter+geeta)
print(harrypotter.pages + geeta.pages)



##program 3

class BookA :
    def __init__(self,pages):
         self.pages = pages
    def __gt__(self,other):
         return self.pages > other.pages

class BookB:
    def __init__(self,pages):
        self.pages = pages


harrypotterA = BookA(1000)
geetaA = BookB(5000)
print(harrypotter + geetaA)




# Method overloading


class calculator:
#     def addition(self,x,y):
#         print(x+y)
#     def addition(self,x,y,z):
#          print(x+y+z)
#      def addition(self,x,y,z,a):
#          print(x+y+z+a)
#
#
# a = calculator()
# a.addition(12,55)
# a.addition(14,55,33)

  def addition(self,x=None, y = None,z=None,a=None):
      if x != None and y != None and z != None and a != None:
          print(x+y+z+a)
          if x != None and y != None and z != None:
              print(x + y + z)
          if x != None and y != None:
              print(x + y)

B= calculator()
B.addition(12,55,55,8)




#method overriding



class Worldbank:
     def loan(self):
      print("i am loan from wb")
     def save(self):
       print("i am loan from wb")

class Sbi(Worldbank):
    def loan(self):
        print("i am loan from Sbi")
    def save(self):
         print("i am loan from Sbi")
wardha = Sbi()
wardha.save()
wardha.loan()





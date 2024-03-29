##progarm1


class Dog:
    def talk(self):
        print("bhow bhow")

class Human:
    def talk(self):
        print("hello hii")
def call_talk(obj):
        obj.talk()

a= Human()
b=Dog()
print(a)

call_talk(a)
call_talk(b)


##program 2

class Dog:
    def talk(self):
        print("bhow bhow")

class Human:
    def sound(self):
        print("hii")

class Duck:
    def sound(self):
        print("quack quack")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()

    else:
        obj.sound()

a = Human()
call_talk(a)

b = Dog()
call_talk(b)


##overloading and overrding

class BookX:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
      return self.pages + other.pages


class BookY:
    def __init__(self,pages):
        self.pages= pages

    def __add__(self, other):
        return self.pages + other.pages


ramayan = BookX(100)
mahabhart= BookY(1522)
print(ramayan +mahabhart)
print(mahabhart+ramayan)

##program 3
#
# class BookX:
#     def __init__(self,pages):
#         self.pages = pages
#
#     def __gt__(self, other):
#        return self.pages >other.pages
#
# class BookY:
#
#     def __init__(self,pages):
#         self.pages = pages
#     def __lt__(self,pages):
#       return self.pages > other.pages
#
# SNEHAL = BookX(144)
# SHAM = BookY(455)
# print(SNEHAL.pages>SHAM.pages)
# print(SNEHAL.pages<SHAM.pages)
# print(SHAM<SNEHAL)
# print(SNEHAL>SHAM)


##program 4

class WorldBank:
    def loan(self):
        print("im loan from wb")

    def save(self):
        print("im save from wb")


class SBI(WorldBank):
    def loan(self):
        print("im loan from SBI")

    def save(self):
        print("im save from SBI")

class PNB(WorldBank):
    def loan(self):
        print("im loan from PNB")

    def save(self):
        print("im save from PNB")



A= SBI()
A.loan()
A.save()


B= PNB()
B.loan()
B.save()


c=WorldBank()
c.loan()
c.save()





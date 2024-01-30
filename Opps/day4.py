##inheritance

class mother:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayname(self):
         print(self.firstname+self.lastname)

class Father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayF(self):
        print(self.firstname+self.lastname)

class Son(mother,Father):
     def __init__(self,fn,ln,sn):
      super().__init__(fn,ln)
      self.sname = sn
     def displayS (self):
      print(self.sname + self.lastname)
snehal =Son("kawadu","kamble","shubu")
print(snehal.firstname)
print(snehal.lastname)
print(snehal.sname)

# Method resolution order


class A(object):
    def method(self):
        print('A class is called')
        super().method()

class B(object):
    def method(self):
        print('B is called')
        super().method()
class C(object):
    def method(self):
        print('C is called')

class X(A,B):
    def method(self):
        print("X is called")
        super().method()
class Y (B,C):
    def method(self):
        print("Y is called")
        super().method()
class P(X,Y,C):
    def method(self):
        print("P is called")
        super().method()





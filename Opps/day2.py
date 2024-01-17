

class Student:
    def __init__(self,fn,ln,adhar):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adhar
    def displayName(self):
        print(self.firstName + self.lastName)

snehal = Student("snehal",'kamble',1544611323)
print(snehal.firstName)
print(snehal.lastName)
print(snehal.adharNo)


class Students:
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age
    def displayName(self):
        print(self.firstName+self.lastName)
nikita = Students("nikita","kamble",26564166)

        
class Teacher:
    def __init__(self,fn,ln,age,salary):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.salary = salary
    def displayname(self):
        print(self.firstname + self.lastname)
    def displaysalary(self):
        print(self.salary)

x = Teacher("shubham","gedam",28,15000)
print(x.salary)
print(x.firstname)
print(x.lastname)
print(x.age)

##program1

class Student:
    def __init__(self,fn,ln,age,):
        self.firstname = fn
        self.lastname = ln
        self.age = age
    def displayname(self):
        print(self.firstname+ self.lastname)


class Teacher(Student):
    salary = 15000
    def displaysalary(self):
        print(self.salary)
y = Teacher("kirtik","kadu",28)
print(y.firstname)
print(y.lastname)
print(y.age)
y.displaysalary()
y.displayname()

##program 2

class Student:
    def __init__(self,fn,ln,age):
        self.firstname = fn
        self.lastname = ln
        self.age = age
    def displayname(self):
        print(self.firstname+self.lastname)


class Teacher(Student):
    def __init__(self,fn,ln,age,salary):
        super().__init__(fn,ln,age)
        self.salary= salary
    def displaysalary(self):
        print(self.salary)

snehal =Teacher("snehal","kamble",25,25000)
print(snehal.firstname)
print(snehal.lastname)
print(snehal.age)
print(snehal.salary)
snehal.displaysalary()
snehal.displayname()

##program3


class Grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGname(self):
        print(self.firstname+self.lastname)

class Father(Grandfather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
def displayFname(self):
          print(self.fname+self.lastname)

class Son(Father):
     def __init__(self,fn,ln,ffn,ssn,):
         super().__init__(fn,ln,ffn)
         self.sname = ssn
     def displaySname(self):
            print(self.sname+self.lastname)


snehal = Son("domaji","KAMBLE","kawadu","snehal")
print(snehal.fname)
print(snehal.firstname)
print(snehal.lastname)
print(snehal.sname)
snehal.displaySname()
snehal.displayGname()











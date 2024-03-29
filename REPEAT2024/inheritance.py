##program1

##single inheritance

##parents -- constructor child no -constructor



class Student:
    def __init__(self,fn,ln,rollno):
        self.firstname = fn
        self.lastname = ln
        self.rollnnumber = rollno

    def displyName(self):
        print(self.firstname + self.lastname)
snehal =Student("snehal","kamble",25)
print(snehal.firstname)
print(snehal.lastname)
print(snehal.rollnnumber)
snehal.displyName()

##program 2

##one parent one child


class Teacher(Student):
    salary = 50000
    def disaplaySalary(self):
        print(self.salary)


sk=Teacher("Snehalk","kamble",5452)
print(sk.salary)
print(sk.firstname)
print(sk.lastname)
print(sk.rollnnumber)

sk.displyName()
sk.disaplaySalary()


##progrm 3
##multiple-level

class Student:
    def __init__(self,fn,ln,adharno):
        self.firstname = fn
        self.lastname = ln
        self.adhar = adharno

    def displayName(self):
        print(self.firstname+self.lastname)


class Teacher(Student):
    def __init__(self,fn,ln,adharno,salary):
        super().__init__(fn,ln,adharno)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)


class professor(Teacher):
    def __init__(self,fn,ln,adharno,salary,spec):
        super().__init__(fn,ln,adharno,salary)
        self.special = spec
    def displaySpecialization(self):
         print(self.special)

snehal= professor("snehal","kamble","4521","50000","English")
print(snehal.firstname)
print(snehal.lastname)
print(snehal.adhar)
print(snehal.salary)

snehal.displaySpecialization()
snehal.displayName()
snehal.displaySalary()


# herarchical inheritance

class Mother:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln ,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
      def __init__(self, fn, ln ,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

      def displayDName(self):
         print(self.dname + self.lastName)

shubu = Son("jyotsna ","kamble","shub")
nikita = Daughter("jyotsna","kamble","nikita")

print(shubu.firstName)
print(shubu.lastName)
print(shubu.sname)
shubu.displayMName()
shubu.displaySName()

print(nikita.firstName)
print(nikita.lastName)
print(nikita.dname)
nikita.displayMName()
nikita.displayDName()

# multiple inheritance

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called .....")
        self.firstName = fn
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Son(Mother,Father):
    def __init__(self, fn, ln , ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def dislaySname(self):
        print(self.sname + self.lastName)


chinmay = Son("kawadu","kamble","sarang")

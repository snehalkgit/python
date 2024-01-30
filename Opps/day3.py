#Single inheritance
class Grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGname(self):
        print(self.firstname + self.lastname)

class Father(Grandfather):
            def __init__(self,fn,ln,ffn):
                super().__init__(fn,ln)
                self.fname = ffn
            def displayFname(self):
              print(self.fname + self.lastname)

snehal=Father("kawadu","kamble","domaji")
print(snehal.lastname)
print(snehal.fname)
print(snehal.firstname)


# Multi-level
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

x = Son("domaji","kamble","kawadu","snehal")
print(x.sname)
print(x.lastName)
x.displaySName()
x.displayFName()
x.displayGName()
print(x.firstName)
print(x.fname)


# # program 3

# Herarchical inheritance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self,fn,ln,ssn):
        super().__init__(fn,ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
    def __init__(self,fn, ln, dn):
         super().__init__(fn,ln)
         self.dname = dn

    def displayDname(self):
        print(self.dname + self.lastName)

class Father:
    def __init__(self, fn, ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName + self.lastName)

class Mother:
    def __init__(self, fn,ln):
        print("Mother constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother, Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn,ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

snehal = Son("kawadu","kamble","snehal")
print(snehal.sname)
print(snehal.lastName)
snehal.displayMName()





class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def display_name(self):
        print(self.firstName+self.lastName)


sk = Person("snehal","kamble")
print(sk.firstName)
print(sk.lastName)

ruhi = Person("rushi", "dane")
print(ruhi.firstName)
print(ruhi.firstName)
print(sk.lastName)
print(sk.lastName)
ruhi.display_name()
sk.display_name()


# program 2

class Person2:
    country = "india"

    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def changeCountry(cls, cnty):
        cls.country = cnty


nk = Person2("niki", "kamble")
sp = Person2("sarika", "pansare")
vrush = Person2('vrushali', "patil")

print(nk.firstName)
print(sp.lastName)
print(nk.country)
nk.country = "bharat"
print(sp.country)
print(nk.country)
print(sp.country)
Person2.changeCountry("Hindustan")
print(vrush.country)
print(nk.country)
print(vrush.country)













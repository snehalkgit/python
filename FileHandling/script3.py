# ##program1
#
# f1 = open('virat-kohli.png','rb')
# f2 = open('virat2.png','wb')
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()
#


##program2
with open('sample.txt','w')as f:
    f.write("im learning js \n")
    f.write("im learning python \n")
with open('sample.txt','r')as f:
    for line in f:
        print(line)

#program3

#python object  -----> binary file -----> serialization
#binary object  ------> python object  - deserialization

class Employee:
    def __init__(self,fn,ln,age,rollno):
        self.firstname = fn
        self.lastname = ln
        self.age = age
        self.rollnum = rollno
snehal=Employee("snehal","kamble",24,8)

import pickle
f= open('emp.dat','wb')
n = int(input('how many employees?'))
for i in range(n):
    fn = input('enter firstname')
    ln = input("enter lastname")
    age=input('enter age')
    rn= input('enter rollno')
    e = Employee(fn,ln,age,rn)
    pickle.dump(e,f)
    f.close()

    import pickle

    f = open('emp.dat', 'rb')
    while True:
        try:
            e = pickle.load(f)
            print(e.firstname)
            print(e.lastname)
            print(e.lastname)
            print(e.lastname)
        except EOFError:
            print("End of file reached")
            break
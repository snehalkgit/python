#compile time error
##runtime error
#logical error

##program1

# def addition(x,y): ##:
#     print(x+y)
#     addition(12,4)



##program2
# x = input("enter the number one")
# y = input("enter the number two")
# print("hello")
# print(int(x)/int(y))
# print("bye")

##program3

def calculateAge(age):
    return age


a = calculateAge(24)
print(a)

#program 4
print("hello")
##print(10/0)
print("bye")

print("hello")
try:
    print(20/0)
except Exception:
    print("Division by zero")
print("hello")

print("----------snehal-------------")
try:
    print(20/5)
    print([11,2255,33,144,25].index(67))
except Exception:
    print("hi")
except Exception:
    print("Bye")
else:
    print('hello')
finally:
    print('result done')









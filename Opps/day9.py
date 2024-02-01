## TOPICS TO BE COVERED

a= 400
b = 4000
##b =0
c=a/b  ##ZeroDivisionError: division by zero
print(c)
print(a)


Name = "snehal"
print(Name)
print(Name[0])
##print(Name[9]) #IndexError: string index out of range


# syntax

# try:
#   code
# except:
#   code
# except:
#   code
# else: # if no error in the code i.e with no exceptions
#   code
# finally:
#  code

a = 1000

try:
  b = 0
  c = a/b
  print(c)
except:
  print("Something went wrong !!!")



##adding more info to the user /code

try:
  b = 0
  c=a/b
  print(c)
except Exception as i_am_eror:
   print("something wrong")


try:
   print(Name[10])
except Exception as e :
    print("something went wrong")

   ##catching multiple exceptions

try:
  b=100
  c=a/b
  print(c)
except Exception as e:
  print("something went wrong")
except Exception as f:
   print("Something went wrong !!!",f)
else:
  print("No error found")
finally:
  print("This line will always get excecuted !!!")

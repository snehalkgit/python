##program 1
from typing import List

A= [1999,1998,1996,1997,1995]
ages=[]
for x in A :
  x1 = 2024 -x
  ages.append(x1)
print(ages)

print([2024-x for x in A]) ## list compreshion

a =list(map(lambda x: 2024-x,A)) ## lambda function
print(a)


##proagrm2
# f = lambda x:2024-x
# print(f)


##program 3

names = ["snehal","samiksha","vrushali","sayli"]
# print(names)

above6 =[]
for x in names:
    if len(x)> 6:
      above6.append(x)
      print(above6)

##list comp

print([x for x in names if len(x)>3])

##lambda function

S=list(filter(lambda x : len(x)> 3,names))
print(S)


##progarm 4
money=[]
M=[1,5,44,55,88,77,-11,-666,-55,-84]
for x in M:
  if x < 0:
   money.append('withdraw')
else:
   money.append("deposit")
   print(money)


  ##list compreshion
print(['WITHDRAW' if x < 0 else "deposite" for x in M])

print(list(filter(lambda x: x > 0, M)))
print(list(filter(lambda x : x < 0 ,M)))
print(list(map(lambda x : x < 0 , M)))










#program1

setA = {22,54,85,66,35,22,84}
setA.pop()  #removing last
print(setA)

#program2

setB = {44,22,11,33}
setB.update((44,58,63))
setB.update({47,55,23})
setB.update([55,87,1,2,3])
print(setB)

#program3

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setA = setC.intersection(setD)  #find the common from both
print(setA)

#progarm4

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setS = setC.union(setD)  #@combine in set from both but not repeated the same value
print(setS)


#program5

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setC.intersection_update(setD) #find common from both
print(setC)

#program 6
setC= {11,55,77,98}
setD = {55,44,11,66,54}
print(setC.difference(setD)) #find  uncommon elements  from both set
print(setD.difference(setC))

#program 7

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setC.difference_update(setD)
print(setC)
setD.difference_update(setC) # removes the items that exist in both sets
print(setD)


#program 8

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setA= setC.symmetric_difference((setD))
print(setA) # returns a set that contains all items from both set,
# but not the items that are present in both sets.

setD.symmetric_difference(setC)
print(setD)


#program 9

setC= {11,55,77,98}
setD = {55,44,11,66,54}
setC.symmetric_difference_update(setD)
print(setC)
# updates the original set by removing items that are present in both sets,
# and inserting the other items.


#program10

setC= {11,55,77,98}
setD = {55,44,11,66,54}
print(setC.issubset(setD)) #true or false return
print(setD.issuperset(setC))

#program 11

setC= {11,55,77,98}
setD = {55,44,11,66,54}
print(setC.isdisjoint(setD))
print(setD.isdisjoint(setC))


#program 12
setC= {11,55,77,98}
setD = {55,44,11,66,54}

setC.remove(77)
print(setC)
#if we give wrong value it gives error

(setC.discard(11))
print(setC)

print(setC.discard(112))
#if we give wrong value it return none values


cities={"goa","mumbai","pune","shimala"}
print(cities)

 #lloop

for item in cities:
     print(item) #loop



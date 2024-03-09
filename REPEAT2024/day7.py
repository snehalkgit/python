setA={44,22,33,45}
setB={45,25,33.45,25}
setC=setA.union(setB)
print(setC)

setE={14,55,22,33,45}
setF={45,25,32,36,25}
setG= setE.intersection(setF)
print(setG)

setE.intersection_update(setF)
print(setF)
print(setE)

##program 2

setQ = {11,22,33}
setE = {45,66,77,33}


setR= setQ.symmetric_difference(setE)
print(setR)

setQ.symmetric_difference_update(setE)
print(setQ)
print(setE)


setQ = {11,22,33,44,48}
setE = {45,66,77,33,11,45}
setQ.difference_update(setE)
print(setQ)

setE.difference_update(setQ)
print(setE)

 ##program 3

setQ = {11,22,33,44,48}
setE = {45,66,77,33,11,45}

A=setQ.issubset(setE)
print(A)

B=setE.issubset(setE)
print(B)


##program 4

setQ = {11,22,33,44,48}
setE = {45,66,77,33,11,45}

C=setQ.isdisjoint(setE)
print(C)

D=setE.isdisjoint(setE)
print(D)

##program 5
setT={14,25,12,22,33}
setT.add(41)
print(setT)

setT.pop()

setT.remove(14)
print(setT)

setT.update({45,25,45,25})
print(setT)


setT.discard(14)
print(setT)











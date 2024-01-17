##program1
birthyear = [1989,1990,1991,1992]
a=[]
for item in birthyear:
    a.append(2023-item)
print(a)

b = [2023-item for item in birthyear]
b=[2023-item for item in birthyear]
print(a)

##program2

numberB = [1,2,3,4,5,6,7,8,9]
c=[item * 2 for item in numberB]
print(c)


numberA = [7,8,4,5,6,9,10]
d=[ item * 3 for item in numberA]
print(d)

for item in numberA:
    d.append(item *3)
print(d)


##program 3
marks = [22,33,44,55,8,41,56,88,74,14,56,15,22]
b=[]
for item in marks:
    if item >40:
        b.append(item)
print(b)

b=[item for item in marks if item >40]
print(b)


c=[item for item in range(len(marks))if marks [item]>40]
print(c)

##program 4
names = ["snehal","kamble","sarika","dipika"]
d=[item [0] for item in names]
print(d)




s = 1
q = 5
if s >q:
    print("s is greater ")
else :
    print("q is greater")
    print("s is greater") if s >q else print("q is greater")

##program 5
A1 = [1,3,2,5,4,5,6,2,5,6,3]
a1 = []
for item in A1:
    if item % 2==0 :
        a1.append("even")
    else :
        a1.append("odd")
        print(a1)


h2=["even" if item % 2 == 0 else "odd" for item in A1]
print(h2)


#####3
listA= [1,4,5]
listB =[1,8,6]
sum=[]
for item in range (len(listA)):
    sum.append(listA[item]*listB[item])
    print(sum)
S = [listA[item] * listB[item] for item in range(len(listA))]
print(s)

numbers2=[4,5,4,7,8,5,6,66]

a=[item *3 for item in numbers2]
print(a)


for item in numbers2:
   q= item *2
   print(q)

q=[item % 2 for item in numbers2]
print(q)



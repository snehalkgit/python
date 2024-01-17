#list comperhension

x = [1,2,3,4,5,6,7,8,9,10]
tableoftwo = []
for  item in x:
    tableoftwo.append(item * 2)
    print(item)


#program2

#{expression loop condition}

x = [1,2,3,4,5,6,7,8,9]
q3=[item * 2 for item in x ]
print(q3)

#program 3

birthyear=[1999,1998,1997,1996]
ages =[]
for x in range (len(birthyear)):
    ag= 2023-birthyear[x]
    ages.append(ag)
    print(ages)


ages2=[2023-item for item in birthyear]
print(ages2)

#program3
#[expression :loop:condition]

marks =[33,55,44,88,45,66,15,45,77,66,25]
above40=[]
for item in marks:
    if item>40:
        above40.append(item)
        print(above40)


above40two=[item for item in marks if item >40]
print(above40two)


#program4
square=[1,4,5,8,7,9,6,5]
squares = [item *item for item  in square]
print(squares)


#program5
names = ["snehal","chiku",'sayli',"rishi"]
capital=[item.upper() for item in names]
print(capital)

#program6

#[odd,even,odd,even]
numbersB  = [33,444,5,6]
even = ["odd" for item in  numbersB if item % 3 == 0]
print(even)


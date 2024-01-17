# conditional statements ---- one input and multiple output
# numT > 0 and num <=5 ===> 10 & discount
# numT >5 and numT <==10 ====> 20 % discount
# numT >10 =====> 30 % discount

# if condition
# pass

marks = 97
if marks > 96:
    print("gradeA")
if marks > 50:
    print("gradeB")
if marks > 78:
    print("gradeC")

numT = 15
if numT > 10 and numT >= 15:
    print('10 % discount')
if numT > 20 and numT >= 25:
    print("20 % discount")
if numT >= 25 and numT <= 50:
    print("30 % discount")

numT = -15
if numT > 10 and numT >= 15:
    print('10 % discount')
elif numT > 20 and numT >= 25:
    print("20 % discount")
elif numT >= 25 and numT <= 50:
    print("30 % discount")
else:
    print("incorrect")

#program
marks = 65
if (marks >= 60):
    print('grade A')
if (marks >= 80):
    print('grade B')
if (marks >= 70):
   print('grade C')

# program 2
p = 10
q = 5
if p > q:
    print("p is greater")
else:
    print("q is greater")

# program
x1 = 10
x2 = 20
x3 = 15
if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")

# TERNARY OPERATOR
d = 4
e = 5
print("d is greater") if d > e else print("e is greater")

age = 10
q1 = "can drive" if age >=18 else "cannot drive"
print(q1)


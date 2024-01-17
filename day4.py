#conditional statements

# discount
# flat 100 rs off
# percentage 10 %
# range discount - 2-5 , 5- 10
# special discount -  coupon

#program 1
numT = 10
if numT > 0 and numT <= 5 :
    print("5 % discount")
if numT>5  and numT<=10:
     print("10 % discount ")
if numT>10:
    print("20 % discount")

#program2
numT = -50
if numT>0 and numT <=5:
    print("5 % discount")
elif numT >5 and numT <=10:
    print("10 % discount")
elif numT >10 and numT<=20:
    print("20 % dicount")
else:
    print('invalid')

#program3
marks = 40
if marks>=40:
    print("grade A")
if marks >= 52:
    print("grade B")
if marks >=60:
    print("grade C")

#elseif
marks = -40
if marks >= 40:
    print("grade A")
elif marks >= 52:
    print("grade B")
elif marks >= 60:
    print("grade C")
else :
    print("try again")

#program4
s = 10
t = 15
if s > t :
    print(" s is greater")
else:
    print("t is greater")

#ternary operator
print("s is greater") if s > t else("t is greater")

p = 15
q = 20
if p > t:
    print(" s is greater")
else :
    print(" q is greater")

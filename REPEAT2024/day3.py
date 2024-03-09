##program 1

# firstname = "snehal"
# lastname = " kamble"
# print(firstname)
# print(lastname)
#
# firstname = 'nikita'
# lastname = """ kamble """



## parogram 2

city = "nagpur"
#1 2 3 4 5 6
# n a g p u r
#-1-2-3-4-5-6

print(city[1::])
print(city[1:2])
print(city[1:6])
print(city[2:5])
print(city[1:-1:1])

##program3

city2= "pune"
print(city2[0])
print(city2[1])
print(city2[2])
print(city2[3])

for x in range(4):
    print(x)
    print(city2[x])

city3="mumbai"
for x in range(len(city3) - 1, -1, -1):
    # print(x)
    print(city3[x])

for x in range(50, 4, -5):
    print(x)

city4 = "nagpur"

for x in range(len(city4)):
    # print(x)
    print(city4[x])

for char in city4:
    print(char)

# program 4
print("in" in "chinmay")

# program5
city5 = "wardha"
# 0  1  2  3  4  5
# w  a  r  d  h  a

i1 = 0
while (i1 < len(city5)):
    # print(i1)
    print(city5[i1])
    i1 = i1 + 1

i2 = len(city5) - 1
while (i2 >= 0):
    print(city5[i2])
    i2 = i2 - 1







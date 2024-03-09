info={
    "firstname":"snehal",
    "lastname":"kamble",
    "age":24

}
print(info)
print(info.get('firstname'))
x= info.setdefault('city','nagpur')
print(x)
print(info)


info=dict.fromkeys(['one','two','three'])
print(info)
students = [
    {
        "firstName":"snehal",
        "lastName":"kamble",
        "age":24,
        "skills":["css","java","js"]
    },
    {
        "firstName":"sayli",
        "lastName":"jogi",
        "age":22,
        "skills":["html","css","js","python"]
    },
    {
        "firstName":"nikita",
        "lastName":"kale",
        "age":23,
        "skills":["html","css","js"]

    }

]
print(students[1]['firstName'])

for x in students:
    print(x['lastName'])



 ##loop
# program 2 # user with python skill
for x in students:
    # print(x['skills'])
    if "python" in x['skills']:
        print(x['lastName'])

# program 3 user with python skills and age > 30

for x in students:
    if x['age'] > 30 and "python" in x['skills']:
        print(x['firstName'], x['age'], x["skills"])

# program 4 name and number of skills
for x in students:
    print(x['firstName'] + ":" + str(len(x['skills'])))

# average age of all students
total = 0
for x in students:
    total = total + x['age']

print(total / len(students))

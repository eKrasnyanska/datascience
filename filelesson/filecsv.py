file = open("data/info.txt")

data = file.read()

"""print(type(data))
print(data)"""

lines = data.splitlines()


keys = lines[0].split(",")
values = lines[1].split(",")

print(keys, values)

student = dict()

index = 0

for index in range(len(keys)):

    key = [index]
    value = [index]

    student[key] = value

print(student)


"""for key in keys:
    print(key)

for value in values:
    print(value)"""


file.close
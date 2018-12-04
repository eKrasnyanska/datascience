import os
import os.path


answer = os.path.exists("C:\\")

print(answer)

answer = os.path.isfile("numbders.txt")
print(answer)

answer = os.path.isdir("data")
print(answer)



file = open("data/names.txt")

#data_in_file = file.read()
#print(data_in_file)

lines = file.readlines()
print(lines)

file.close()

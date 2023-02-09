file = open('01_Hello_World.py','r')

# print(file.readable())
# print(file.read())
# print(file.readline())
# print(file.readlines())
print(file.readlines()[2])

file.close()
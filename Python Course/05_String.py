# \n : untuk break line
print("My Name \n is Thor")

# Kalau pake r maka \n nya jadi string
print(r"My Name \nis Thor")

# Agar lebih rapih pake end
print("My Name is Thor",end = "\n")
print("My Name is Thor")

# To Make It Lower Case
name = "My name is Loki"
print(name.lower())

# To Make It Upper Case
print(name.upper())

# To Know Length of the string
print(len(name))

# To Know Index of the string
print(name[1])
print(name[0:1])
print(name[:6])
print(name[1:])
print(name[1:10:3])

# To Reverse The String
print(name[::-1])

# To Know index of specific
print(name.index("a"))
print(name.index("Loki"))

# To Replace With
print(name.replace("a","e"))
print(name.replace("m","Thor"))
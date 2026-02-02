
file = open("data.txt", "w")
file.write("Python file handling.")
file.close()


file = open("data.txt", "r")
c = file.read()
file.close()

print("File content:")
print(c)

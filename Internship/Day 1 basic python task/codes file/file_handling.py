# File Handling

# Writing to a file

file = open("student.txt", "w")
file.write("Ali\n")
file.write("Python Programming")
file.close()

# Reading from the file

file = open("student.txt", "r")
content = file.read()
print(content)
file.close()
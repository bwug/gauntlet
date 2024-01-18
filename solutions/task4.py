# Creating a file and writing to it
with open("file.txt", "w") as file:
    file.write("Hello world")

# Reading from a file
with open("file.txt", "r") as file:
    print(file.read())

# "a" makes .write append to the file's data
with open("file.txt", "a") as file:
    file.write("\nHello world 2")
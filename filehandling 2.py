f = open ("test.txt", "a")
f.write("\nThis text will be appended the content of our file")

f = open("test.txt")
print(f.read())

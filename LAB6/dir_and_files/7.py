f = open("LAB6\dir_and_files\check.txt", "r")
d = open("LAB6\dir_and_files\ccc.txt", "a")
for x in f:
    d.write(x)
f.close()
d.close()
d = open("LAB6\dir_and_files\ccc.txt", "r")
print(d.read())
f = open("LAB6\dir_and_files\clear.txt", 'a')
words = ['hello', 'how', 'are', 'you']
for x in words:
    f.write(x + ' ')
f.close()
f = open("LAB6\dir_and_files\clear.txt", 'r')
print(f.read())
f = open("LAB6\dir_and_files\check.txt", 'r')
cnt = 0
for x in f:
    cnt += 1
print("lines in the file: {}".format(cnt))
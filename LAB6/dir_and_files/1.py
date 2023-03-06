import os
# path = str(input())
path = os.getcwd()

def getDir():
    direc = []
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)):
            direc.append(x)
    return direc

def getFiles():
    files = []
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)) == 0:
            files.append(x)
    return files

def getAll():
    return os.listdir(path)

print(getDir())
print(getFiles())
print(getAll())
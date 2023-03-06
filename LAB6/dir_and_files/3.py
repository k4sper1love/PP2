import os
path = r"C:\Users\kasper\Documents\github\PP2\LAB6\dir_and_files\check.txt"

def check():
    if os.path.exists(path):
        print("File name: {}".format(os.path.splitext(os.path.basename(path))[0]))
        print("Directory name: {}".format(os.path.basename(os.path.dirname(path))))
    else:
        return print("This path does not exist")

check()

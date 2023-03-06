import os
path = r"C:\Users\kasper\Documents\github\PP2\LAB6\dir_and_files\check.txt"

def check_path():
    if os.path.exists(path): print("This path exists")      
    else: 
        return print("This path does not exist")
    
    if os.access(path, os.R_OK): print("read: OK")
    else: print("read: NO")

    if os.access(path, os.W_OK): print("write: OK")
    else: print("write: NO")

    if os.access(path, os.X_OK): print("executed: OK")
    else: print("executed: NO")

check_path()
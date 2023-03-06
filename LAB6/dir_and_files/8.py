import os
path = r"C:\Users\kasper\Documents\github\PP2\LAB6\dir_and_files\plsdeleteme.txt"

def removeFile():
    if os.path.exists(path): print("This path exists")      
    else: 
        return print("This path does not exist")
    
    if os.access(path, os.R_OK): print("read: OK")
    else: return print("read: NO")

    if os.access(path, os.W_OK): print("write: OK")
    else: return print("write: NO") 

    if os.access(path, os.X_OK): print("executed: OK")
    else: return print("executed: NO")

    os.remove(path)
    return print("file deleted!")
removeFile()
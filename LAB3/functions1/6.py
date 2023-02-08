def reverseStr(str):
    newstr = str.split()
    newstr.reverse()
    for x in newstr:
        print(x, end = " ")

inpStr = input()
reverseStr(inpStr)
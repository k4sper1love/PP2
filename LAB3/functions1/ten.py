def unique(mylist):
    newlist = []
    mylist.sort()
    for i in range(len(mylist)):
        if i == 0:
            continue
        if mylist[i] == mylist[i-1]:
            continue
        else:
            newlist.append(mylist[i])
    return newlist

# mylist = [int(x) for x in input().split()]
# print(unique(mylist))
class numbers:
    def __init__(self, mylist):
        self.list = list(mylist)
        self.border = round(max(mylist) ** 0.5)
    
    def filterPrime(self):
        for i in range(2, self.border + 1):
            self.list = list(filter(lambda x: (x == i or x % i != 0) and x != 1, self.list))
        return self.list
        
newList = numbers(list(range(100)))
print(newList.filterPrime())
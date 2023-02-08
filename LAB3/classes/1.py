class strClass:
    def __init__(self):
        self.inputStr = ''
    def getString(self):
        self.inputStr = str(input())
    def printString(self):
        print(self.inputStr.upper())

test = strClass()
test.getString()
test.printString()
str = "Hello. How Are You?"
upperCase = 0
lowerCase = 0
for x in str:
    # if x.isupper():
    #     upperCase += 1
    # elif x.islower():
    #     lowerCase += 1
    if ord(x) >= 65 and ord(x) <= 90:
        upperCase += 1
    elif ord(x) >= 97 and ord(x) <= 122:
        lowerCase += 1
print("lower case: {}, upper case: {}".format(lowerCase, upperCase))


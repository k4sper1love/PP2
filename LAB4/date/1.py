import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-{} %X.%f").format(int(x.strftime("%d"))- 5))

# OR
print(x - datetime.timedelta(days = 5))
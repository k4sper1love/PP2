import datetime
x = datetime.datetime.now()
print("Yesterday: {},\nToday: {},\nTomorrow: {}.".format(x - datetime.timedelta(days = 1), x, x + datetime.timedelta(days = 1)))
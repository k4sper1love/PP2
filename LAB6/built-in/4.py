import time
def time_root(num, ms):
    time.sleep(ms//1000)
    print("Square root of {} after {} miliseconds is {}".format(num, ms, num ** 0.5))
time_root(int(input("num: ")), int(input("ms: ")))
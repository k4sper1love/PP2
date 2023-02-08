def filter_prime(list):
    for x in list:
        if x == 1:
            continue
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print("{} - is prime".format(x))
numbers = [int(x) for x in input().split()]
filter_prime(numbers)
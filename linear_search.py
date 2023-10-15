import time
import random


def linear_search(k, array):
    j = 0
    l = 0
    for i in range(0, len(k)):
        if k[i] in array:
            l = l+1
    if l == len(k):
        return "search complete"


def number_generation(max):
    a = []
    while len(a) < max:
        y = random.randint(1, max)
        if y not in a:
            a.append(y)
    return a


if __name__ == "__main__":
    start = time.time()
    size = int(input("Enter ur data size"))
    keys = number_generation(size)
    box = range(0, 10000, 1)
    msg = linear_search(keys, box)
    print(msg)
    end = time.time()
    print(end-start)




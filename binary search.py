def binary_search(lis, num):
    le = 0
    h = len(lis) - 1
    m = 0
    flag = 0

    while le <= h:

        m = (le + h) // 2

        if num > lis[m]:
            h = m - 1

        elif num < lis[m]:
            le = m + 1

        else:
            flag = 1
            return m

    if flag == 0:
        return "not found"

if __name__ == "__main__":
    num = int(input("enter ur key to find"))
    lis = range(10000, 0, -1)
    le = 0
    h = len(lis)-1
    result = binary_search(lis, num)
    print(result)



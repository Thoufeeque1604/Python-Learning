from itertools import permutations


def permu(s, n):
    f = permutations(s, n)

    for i in f:
        print(i)


if __name__ == "__main__":
    s = input().split(" ")
    n = int(input())
    permu(s, n)
    #print(s)

'''from itertools import permutations

# Get all permutations of length 2
# and length 2
perm = permutations([1, 2, 3], 2)

# Print the obtained permutations
for i in list(perm):
    print (i)'''
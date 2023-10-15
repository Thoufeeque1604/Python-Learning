'''import random

a = []
i = 0
while len(a)<10:
    y = random.randint(1, 10)
    if y not in a:
        a.append(y)


print(a)'''

import random

'''# Set the range of random integers
min_int = 0
max_int = 99

# Generate 10000 random unsorted integers
random_numbers = [random.randint(min_int, max_int) for i in range(100)]

# Print the generated random numbers
print(random_numbers)
'''
#def number_generation(max):
a = []
while len(a) < 100:
    y = random.randint(1, 100)
    if y not in a:
        a.append(y)
print(a)


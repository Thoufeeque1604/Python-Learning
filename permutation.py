import itertools

# List of all 25 persons
persons = ['A','B','C','D','E','F','G','H','I','J','K','L'
           ]

# Number of persons in each shift
shift1_size = 5
shift2_size = 6

# Generate all possible combinations of persons for shift 1 and shift 2
shift1_permutations = list(itertools.permutations(persons, shift1_size))
shift2_permutations = list(itertools.permutations([person for person in persons if person not in shift1_permutations], shift2_size))

# Generate all possible permutations of the combinations for the final schedule
schedule_permutations = list(itertools.product(shift1_permutations, shift2_permutations))

# Print all possible schedules
for schedule in schedule_permutations:
    print(schedule)

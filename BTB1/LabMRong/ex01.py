import itertools

lst = [1, 2, 3]
permutations = list(itertools.permutations(lst))

for p in permutations:
    print(p)
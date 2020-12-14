from itertools import permutations


def possible_permutations(my_list):
    for p in permutations(my_list):
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]

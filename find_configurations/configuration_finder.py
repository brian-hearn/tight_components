from itertools import combinations, permutations
from fconf_checking_functions import *

def generate_3_subsets(n):
    # Generate all 3-element subsets of the ground set {0, ..., n-1}
    ground_set = set(range(n))
    return [frozenset(c) for c in combinations(ground_set, 3)]

def canonical_form(family, ground_set):
    # Compute the canonical form of a family under all permutations of the ground set
    perms = permutations(ground_set)
    min_form = None
    for p in perms:
        mapping = dict(zip(ground_set, p))
        relabeled = [frozenset(mapping[x] for x in subset) for subset in family]
        sorted_family = sorted([tuple(sorted(s)) for s in relabeled])
        if min_form is None or sorted_family < min_form:
            min_form = sorted_family
    return tuple(min_form)

def generate_spanning_families_with_triplets(n, max):
    # Generate all spanning families of 3-element subsets (triplets) of a ground set of size n
    ground_set = set(range(n))
    triplets = generate_3_subsets(n)

    unique_canonicals = dict()

    for r in range(1, len(triplets) + 1):
        print('Checking size ' + str(r))
        if r <= max:
            for family in combinations(triplets, r):
                if not is_spanning(family, ground_set):
                    continue
                canon = canonical_form(family, ground_set)
                unique_canonicals[canon] = r

    return unique_canonicals
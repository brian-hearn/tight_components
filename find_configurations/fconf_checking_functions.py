from collections import Counter
from itertools import combinations

def is_spanning(family, ground_set):
    # Check if the union of all sets in the family equals the ground set
    return set().union(*family) == ground_set

def count_repeated_pairs(family):
    # Count how many pairs of elements appear in at least two different triples in the family
    pair_counter = Counter()
    for triple in family:
        for pair in combinations(triple, 2):
            pair = tuple(sorted(pair))
            pair_counter[pair] += 1
    return sum(1 for count in pair_counter.values() if count >= 2)

def count_quadruples_with_multiple_triples(family, n):
    # Count how many 4-element subsets of {0..n-1} contain at least two triples from the family
    quadruple_count = 0
    all_quadruples = combinations(range(n), 4)
    family_sets = [set(triple) for triple in family]

    for quad in all_quadruples:
        quad_set = set(quad)
        count = sum(1 for triple in family_sets if triple <= quad_set)
        if count >= 2:
            quadruple_count += 1

    return quadruple_count
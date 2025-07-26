#############################################################
### script for finding valid monochromatic configurations ###
#############################################################
from collections import defaultdict
from configuration_finder import *

# number of vertices
n = 6
# maximum number of triples allowed in each configuration
max = 6
# count pairs which appear in at least three triples in each configuration
count_triple_repeats = True

families = generate_spanning_families_with_triplets(n, max)
grouped = defaultdict(list)
for family, size in families.items():
    grouped[size].append(family)

# Print grouped families and analysis
for size in sorted(grouped):
    print(f"\n--- Families of size {size} ---")
    for family in sorted(grouped[size]):
        print(f"Family: {family}")
        num_repeated_pairs = count_repeated_pairs(family, 2)
        print(f"  Pairs appearing at least 2 times: {num_repeated_pairs}")
        if count_triple_repeats:
            num_3x_repeated_pairs = count_repeated_pairs(family, 3)
            print(f"  Pairs appearing at least 3 times: {num_3x_repeated_pairs}")
        num_quadruples_with_multiple_triples = count_quadruples_with_multiple_triples(family, n)
        print(f"  Quadruples containing at least 2 triples: {num_quadruples_with_multiple_triples}")
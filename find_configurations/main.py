#############################################################
### script for finding valid monochromatic configurations ###
#############################################################
from collections import defaultdict
from configuration_finder import *

# number of vertices
n = 6
# maximum number of triples allowed in configuration
max = 4

families = generate_spanning_families_with_triplets(n, max)
grouped = defaultdict(list)
for family, size in families.items():
    grouped[size].append(family)

# Print grouped families and analysis
for size in sorted(grouped):
    print(f"\n--- Families of size {size} ---")
    for family in sorted(grouped[size]):
        num_repeated_pairs = count_repeated_pairs(family)
        num_quadruples_with_multiple_triples = count_quadruples_with_multiple_triples(family, n)
        print(f"Family: {family}")
        print(f"  Repeated pairs: {num_repeated_pairs}")
        print(f"  Quadruples with ≥2 triples: {num_quadruples_with_multiple_triples}")
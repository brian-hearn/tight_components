#############################################################
### script for finding valid monochromatic configurations ###
#############################################################
from collections import defaultdict
from configuration_finder import *
import pandas as pd
import os

# number of vertices
n = 6
# maximum number of triples allowed in each configuration
max = 50
# count pairs which appear in at least three triples in each configuration
count_triple_repeats = True

# print results to console?
print_results = True
# output as .csv?
output_as_csv = True
csv_name = "7col_fullconfigtable"

families = generate_spanning_families_with_triplets(n, max)
grouped = defaultdict(list)
for family, size in families.items():
    grouped[size].append(family)

###############################
### Print output to console ###
###############################

# Print grouped families and analysis
if print_results:
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

######################
### Output as .csv ###
######################

if output_as_csv:
    data_rows = []
    for size in sorted(grouped):
        for family in sorted(grouped[size]):
            row = {
                "Family Size": size,
                "Family": tuple(family),  # ensure hashable/printable format
                "Pairs ≥ 2x": count_repeated_pairs(family, 2),
                "Quadruples with ≥2 Triples": count_quadruples_with_multiple_triples(family, n)
            }
            if count_triple_repeats:
                row["Pairs ≥ 3x"] = count_repeated_pairs(family, 3)
            data_rows.append(row)

    # Create DataFrame
    df = pd.DataFrame(data_rows)

    # Reorder columns
    columns = ["Family Size", "Family", "Pairs ≥ 2x"]
    if count_triple_repeats:
        columns.append("Pairs ≥ 3x")
    columns.append("Quadruples with ≥2 Triples")
    df = df[columns]

    # Save CSV in the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, csv_name + ".csv")
    df.to_csv(output_path, index=False)

import itertools
import pandas as pd

def find_partitions(df, sizes_used, total):
    unique_sizes = sorted(df['Family Size'].unique())
    
    # Generate combinations with replacement (order doesn't matter)
    combos = itertools.combinations_with_replacement(unique_sizes, sizes_used)
    
    # Filter combos whose sum equals total
    valid_combos = [combo for combo in combos if sum(combo) == total]
    
    return valid_combos


# df = pd.DataFrame({'size': [2, 3, 4]})
# result = find_partitions(df, sizes_used=3, total=9)
# cleaned_output = [tuple(int(x) for x in combo) for combo in result]
# print(cleaned_output)

import pandas as pd
import numpy as np
import itertools

def find_valid_combinations(df, k, constraints):
    """
    Efficiently finds all combinations of exactly k rows such that each specified column
    satisfies a 'min' or 'exact' constraint on the sum.

    Parameters:
        df (pd.DataFrame): The DataFrame to process.
        k (int): Number of rows to choose.
        constraints (dict): { column_name: ('min' or 'exact', value), ... }

    Returns:
        list of tuple: Each tuple contains the DataFrame indices of a valid combination.
    """
    columns = list(constraints.keys())
    data = df[columns].to_numpy()  # shape: (n_rows, n_columns)
    index_array = df.index.to_numpy()
    col_indices = {col: i for i, col in enumerate(columns)}
    valid_combos = []

    for combo in itertools.combinations(range(len(df)), k):
        rows = data[list(combo)]               # shape: (k, n_columns)
        col_sums = rows.sum(axis=0)            # shape: (n_columns,)

        # Check all constraints
        if all(
            (typ == 'min' and col_sums[col_indices[col]] >= val) or
            (typ == 'exact' and col_sums[col_indices[col]] == val)
            for col, (typ, val) in constraints.items()
        ):
            valid_combos.append(tuple(index_array[i] for i in combo))

    return valid_combos

input_file = 'output.csv'
df = pd.read_csv(input_file)

# # Example dataframe
# data = {
#     'A': [1, 2, 3, 4],
#     'B': [5, 1, 2, 3],
#     'C': [10, 10, 10, 10],  # Irrelevant
# }
# df = pd.DataFrame(data)

# Constraints:
# - Column A must sum exactly to 5
# - Column B must be at most 6
constraints = {
    'Family Size': ('exact', 35),
    'Pairs filled': ('min', 21),
    'Quadruples with ≥2 Triples': ('min', 35)
}
# Find all valid 2-row combinations
valid_combos = find_valid_combinations(df, k=2, constraints=constraints)

print("Valid combinations (row indices):", valid_combos)


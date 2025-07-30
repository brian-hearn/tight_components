import numpy as np
import itertools

def print_constraints(df, constraints):
    # Get numeric columns (excluding 'size' column)
    numeric_cols = df.iloc[:, 1:].select_dtypes(include=[np.number]).columns.tolist()

    print("Constraints:")
    for col_name, target_value, mode in constraints:
        if col_name in numeric_cols:
            if mode == 'min':
                comp_str = ">="
            elif mode == 'max':
                comp_str = "<="
            elif mode == 'equal':
                comp_str = "=="
            else:
                comp_str = f"[Unknown mode '{mode}']"
            print(f" - Sum of '{col_name}' {comp_str} {target_value}")
        else:
            print(f" - Constraint refers to invalid or non-numeric column '{col_name}'")

def find_valid_combinations(df, sizes_list, constraints):
    # Extract the 'size' column
    size_col = df.iloc[:, 0].to_numpy()

    # Select numeric columns only (excluding 'size')
    numeric_df = df.iloc[:, 1:].select_dtypes(include=[np.number])
    numeric_cols = numeric_df.columns.tolist()
    param_array = numeric_df.to_numpy(dtype=float)

    # Map column names in constraints to numeric indices
    constraints_mapped = []
    for col_name, target, mode in constraints:
        if col_name not in numeric_cols:
            raise ValueError(f"Column '{col_name}' not found among numeric columns: {numeric_cols}")
        col_index = numeric_cols.index(col_name)
        constraints_mapped.append((col_index, target, mode))

    # Find candidate rows per size
    row_options_per_size = []
    for size in sizes_list:
        matches = np.flatnonzero(size_col == size)
        if matches.size == 0:
            return []  # no valid combos if a size has no matching rows
        row_options_per_size.append(matches)

    valid_combinations = []

    for combo in itertools.product(*row_options_per_size):
        # print(combo)
        selected_rows = param_array[np.array(combo)]
        col_sums = np.sum(selected_rows, axis=0)

        passed = True
        for col_index, target, mode in constraints_mapped:
            val = col_sums[col_index]
            if mode == 'max' and val > target:
                passed = False
                break
            elif mode == 'min' and val < target:
                passed = False
                break
            elif mode == 'equal' and not np.isclose(val, target):
                passed = False
                break

        if passed:
            valid_combinations.append(combo)

    return valid_combinations

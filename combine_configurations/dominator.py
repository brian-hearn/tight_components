import pandas as pd

def remove_dominated_rows(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure we don't modify the original DataFrame
    df = df.copy()

    # Result container
    result_rows = []

    # Group by each unique Family size
    for size, group in df.groupby('Family Size'):
        print(group)
        # Remove duplicates and preserve original index
        group = group.drop_duplicates().reset_index()

        # Columns to compare (exclude 'Family size' and the original index)
        compare_cols = [col for col in group.columns if col not in ['Family Size', 'index']]

        # Mask to track non-dominated rows
        non_dominated_mask = [True] * len(group)

        for i in range(len(group)):
            for j in range(len(group)):
                if i != j and non_dominated_mask[i]:
                    # Check if row j dominates row i
                    if all(group.iloc[j][col] >= group.iloc[i][col] for col in compare_cols):
                        if any(group.iloc[j][col] > group.iloc[i][col] for col in compare_cols):
                            non_dominated_mask[i] = False
                            break

        # Keep only non-dominated rows, recover original indices
        kept_indices = group.loc[non_dominated_mask, 'index']
        result_rows.append(df.loc[kept_indices])

    # Combine results and reset index
    return pd.concat(result_rows, ignore_index=True)

# df = pd.DataFrame({
#     'Family size': [3, 3, 3, 3, 4, 4],
#     'A': [1, 2, 2, 3, 1, 2],
#     'B': [1, 2, 3, 1, 2, 2]
# })

# cleaned_df = remove_dominated_rows(df)
# print(cleaned_df)
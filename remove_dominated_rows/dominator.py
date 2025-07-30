import pandas as pd
from typing import List

def remove_dominated_rows(df: pd.DataFrame, compare_cols: List[str]) -> pd.DataFrame:
    df = df.copy()
    result = []

    for size, group in df.groupby('Family Size'):
        # Remove duplicates
        group = group.drop_duplicates(subset=compare_cols).reset_index()

        keep_mask = [True] * len(group)

        for i in range(len(group)):
            for j in range(len(group)):
                if i == j or not keep_mask[i]:
                    continue
                row_i = group.iloc[i]
                row_j = group.iloc[j]

                # Check if row_i is dominated by row_j
                if all(row_i[col] <= row_j[col] for col in compare_cols) and \
                   any(row_i[col] < row_j[col] for col in compare_cols):
                    keep_mask[i] = False
                    break

        # Keep original rows by their index
        kept_indices = group.loc[keep_mask, 'index']
        result.append(df.loc[kept_indices])

    return pd.concat(result, ignore_index=True)

df = pd.DataFrame({
    'Family Size': [2, 3, 3],
    'a': [0, 0.5, 0],
    'b': [0, 1, 0],
    'c': [0, 1, 0],
    'd': [0, 1, 0],
    'e': [0, 0, 0],
    'description': [
        "((0, 1, 2), (0, 1, 3), (2, 4, 5))",
        "((0, 1, 2), (0, 3, 4), (1, 3, 5))",
        "((0, 1, 2), (0, 3, 4), (1, 3, 5))"
    ]
})

# 2,0.0,0,0,0,0,"((0, 1, 2), (3, 4, 5))"
# 3,0.5,1,1,1,0,"((0, 1, 2), (0, 1, 3), (2, 4, 5))"
# 3,0.0,0,0,0,0,"((0, 1, 2), (0, 3, 4), (1, 3, 5))"


filtered = remove_dominated_rows(df, compare_cols=['a', 'b'])
print(filtered)

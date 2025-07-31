from find_combinations import *
from find_partitions import *
import pandas as pd
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script lives
csv_path = os.path.join(script_dir, '7col_smallconfigtable.csv')
df = pd.read_csv(csv_path)

def adjust_columns_by_family_size(df, columns_with_ratios):
    """
    Adjusts specified columns by subtracting 'Family Size' * column-specific ratio from each row.
    Keeps only the adjusted columns and the 'Family' column (if present).

    Parameters:
    - df: pandas DataFrame
    - columns_with_ratios: dict with {column_name: ratio}

    Returns:
    - A modified copy of the DataFrame
    """
    df = df.copy()

    # Check for required columns
    if 'Family Size' not in df.columns:
        raise ValueError("'Family Size' column not found in DataFrame.")

    for col, ratio in columns_with_ratios.items():
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")
        df[col] = round(df[col] - df['Family Size'] * ratio,3)
    
    df['Family Size'] -= 5
    
    columns_to_keep = []
    columns_to_keep.append('Family Size')
    columns_to_keep.extend(columns_with_ratios.keys())
    columns_to_keep.append('Family')
    # Return only the relevant columns
    return df[columns_to_keep]

ratios = {
    'Pairs filled': 0.6,
    'Quadruples with ≥2 Triples': 1
}

adjusted_df = adjust_columns_by_family_size(df, ratios)

# Save CSV in same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, '7col_normalisedsmallconfigtable.csv')
adjusted_df.to_csv(output_path, index=False)
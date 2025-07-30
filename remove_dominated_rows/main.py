import os
from removal_function import *
import pandas as pd  # Make sure pandas is imported

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script lives

csv_path = os.path.join(script_dir, '7col_fullconfigtable.csv')
df = pd.read_csv(csv_path)

small_df = remove_dominated_rows(df, ["Pairs filled", "Quadruples with ≥2 Triples"])

output_file = os.path.join(script_dir, '7col_smallconfigtable.csv')  # save in script folder
small_df.to_csv(output_file, index=False)
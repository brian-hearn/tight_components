from find_combinations import *
from find_partitions import *
import pandas as pd
import os
from dominator import *

# df = pd.DataFrame({
#     'size': [1, 1, 2, 2],
#     'param1': [3, 4, 2, 5],
#     'param2': [1, 2, 3, 1]
# })

sizes_list = [20,5,2,2,2,2,2]

constraints = [
    ['Pairs filled', 21, 'min'],
    ['Quadruples with ≥2 Triples', 35, 'min']
]

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script lives
csv_path = os.path.join(script_dir, 'myoutput.csv')
df = pd.read_csv(csv_path)
# print(df.head())

small_df = remove_dominated_rows(df)
print(len(df))
print(len(small_df))

partitions = find_partitions(small_df, sizes_used=7, total=35)
cleaned_partitions = [tuple(int(x) for x in combo) for combo in partitions]

valid_partitions = []
# for i in range(len(cleaned_partitions)):
for i in range(250):
    print('Checking partition ' + str(i) + ' of ' + str(len(cleaned_partitions)) + '.')
    valid_combinations = find_valid_combinations(small_df, cleaned_partitions[i], constraints)
    cleaned_output = [tuple(int(x) for x in combo) for combo in valid_combinations]
    if cleaned_output:
        valid_partitions.append(cleaned_partitions[i])
    print(cleaned_output)

print_constraints(small_df, constraints)
print('Number of partitions checked: ' + str(len(cleaned_partitions)))
print('Number of valid partitions: ' + str(len(valid_partitions)))
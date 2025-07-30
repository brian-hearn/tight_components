from find_combinations import *
from find_partitions import *
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script lives
csv_path = os.path.join(script_dir, '7col_smallconfigtable.csv')
df = pd.read_csv(csv_path)
# print(df.head())

constraints = [
    ['Pairs filled', 21, 'min'],
    ['Quadruples with ≥2 Triples', 35, 'min']
]

partitions = find_partitions(df, sizes_used=7, total=35)
cleaned_partitions = [tuple(int(x) for x in combo) for combo in partitions]

valid_partitions = []
# for i in range(len(cleaned_partitions)):
for i in range(250):
    print('Checking partition ' + str(i) + ' of ' + str(len(cleaned_partitions)) + '.')
    valid_combinations = find_valid_combinations(df, cleaned_partitions[i], constraints)
    cleaned_output = [tuple(int(x) for x in combo) for combo in valid_combinations]
    if cleaned_output:
        valid_partitions.append(cleaned_partitions[i])
    print(cleaned_output)

print_constraints(df, constraints)
print('Number of partitions checked: ' + str(len(cleaned_partitions)))
print('Number of valid partitions: ' + str(len(valid_partitions)))
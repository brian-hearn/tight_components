from find_combinations import *
from find_partitions import *
import pandas as pd
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script lives
csv_path = os.path.join(script_dir, '7col_smallconfigtable.csv')
df = pd.read_csv(csv_path)
# print(df.head())

constraints = [
    ['Pairs filled', 21, 'min'],
    ['Quadruples with ≥2 Triples', 35, 'min']
]

partitions = [[5,5,5,5,5]]
valid_partitions = []
# for i in range(len(cleaned_partitions)):
for i in range(len(partitions)):
    print('Checking partition ' + str(i+1) + ' of ' + str(len(partitions)) + '.')
    valid_combinations = find_valid_combinations(df, partitions[i], constraints)
    cleaned_output = [tuple(int(x) for x in combo) for combo in valid_combinations]
    if cleaned_output:
        valid_partitions.append(partitions[i])
    print(cleaned_output)

print_constraints(df, constraints)
print(str(len(valid_partitions)) + ' out of ' + str(len(partitions)) + ' partitions are valid.')
# 1: Using core csv module.
import csv
rows = 0
with open('.csv-file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, skipinitialspace=True)
    for row in csvreader:
        rows += 1
print(rows)

# # 2: Using external pandas module.
# import pandas
# content = pandas.read_csv(".csv-file.csv"); # returns DataFrame
# print(len(content) + 1)

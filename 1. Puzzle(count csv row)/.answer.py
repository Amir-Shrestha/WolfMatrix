# # 1: Using core csv module.
# import csv
# rows = 0
# with open('.csv-file.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, skipinitialspace=True)
#     for row in csvreader:
#         rows += 1
# print(rows)

# # 2: Using external pandas module.
# import pandas
# content = pandas.read_csv(".csv-file.csv"); # returns DataFrame
# print(len(content) + 1)


# 3.Scratch Python Logic:
csv_file1 = open('./.csv-file.csv')
modified_record_list = [];
boolean = False;
temp_list = []
for record in csv_file1:
    if(record.count('"') == 1 or boolean ==True):
        print("1")
        if(record.count('"') == 1):
            boolean = not boolean;
        print(boolean)
        temp_list.append(record);
        if(boolean == True):
            continue;
        else:
            modified_record_list.append(temp_list)
            temp_list = []
    else:
        modified_record_list.append(record)
# print(modified_record_list)
print(len(modified_record_list))

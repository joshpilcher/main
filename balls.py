import csv

str_category = "Category"
unique_list = []
category_count = {}
file_infile = open("Google Play Store.csv", "r")
csv_dict_reader = csv.DictReader(file_infile)

for row in csv_dict_reader:
    category = row["Category"]
    if category not in unique_list:
        unique_list.append(category)
        category_count[category] = 1 
    else: 
        category_count[category] += 1 

for category, count in category_count.items():
    print(category, count)
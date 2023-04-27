#2. c)
def unique_count(file_name, header):
 """Displays the unique values along with how many rows they appear in, based on
file_name
 and header"""
 unique_list = []
 row_count = []
 file_infile = open(file_name, "r") as file_infile:
 csv_reader = csv.DictReader(file_infile)
 for lst_cols in csv_reader:
 value = lst_cols[header]
 if value not in unique_list:
 unique_list.append(value)
 row_count.append(1)
 else:
 index = unique_list.index(value)
 row_count[index] += 1
 for i in range(len(unique_list)
 file_infile.close()
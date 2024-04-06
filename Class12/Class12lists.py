data = [[45,56,89],[67,34,78],[23,67,34]]


data_columns = []

for i in range(len(data[0])):
    temp_list = []
    for my_columns in data:
        temp_list.append(my_columns[i])
    data_columns.append(temp_list)
print(data_columns)
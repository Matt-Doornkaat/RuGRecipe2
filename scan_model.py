import pandas as pd

file_name = "recipes.csv"
file = open(file_name)

recipes_df = pd.read_csv(file, index_col=[0], header=[0])

search_command = ["kip", "ui", "wortel"]


my_result = []
my_present = 0
my_absent = 1000

for index, row in recipes_df.iterrows():
    present = 0
    absent = 0

    for i in search_command:

        if i in row[1]:
            present += 1
        else:
            absent += 1

    if absent < my_absent:
        my_result.clear()
        my_result.append(row[0])
        my_absent = absent
    elif absent == my_absent:
        my_result.append(row[0])
    else:
        my_present += 1

    if len(my_result) >= 10:  # if there 10 recipes in the results, stop adding more
        break

print(my_result)

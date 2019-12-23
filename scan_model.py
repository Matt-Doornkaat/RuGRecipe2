import pandas as pd


def scan_recipes(search_command, database="recipes.csv"):

    """
        Search command should be given as a list:
        e.g. ("kip", "ui", "wortel")
    """

    file = open(database)

    recipes_df = pd.read_csv(file, header=[0])

    my_result = {}
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
            my_result.update({row[0]: row[2]})
            my_absent = absent
        elif absent == my_absent:
            my_result.update({row[0]: row[2]})
        else:
            my_present += 1

        if len(my_result) >= 10:  # if there 10 recipes in the results, stop adding more
            break

    return my_result


# EXAMPLE
my_ingredients = ["kip", "ui", "wortel"]
to_cook = scan_recipes(my_ingredients)
print(to_cook)

# to use this function: "from (folder) import scan_model"

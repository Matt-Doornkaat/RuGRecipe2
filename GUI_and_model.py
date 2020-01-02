import pandas as pd
from tkinter import *
import webbrowser


class Interface:

    def __init__(self, master):
        self.master = master
        master.title("Foodscanner")
        master.geometry('560x380')
        master.resizable(False, False)

        # Labels GUI
        label_ingredient = Label(master, text="Ingredient 3", font=("arial", 10, "bold"))
        label_overview = Label(master, text="Ingredients:", font=("arial", 10, "bold"))
        label_suggested = Label(master, text="Suggested recipes:", font=("arial", 10, "bold"))

        # Listbox GUI
        listbox_overview = Listbox(master, width=40, height=15, selectmode='single')
        listbox_recipes = Listbox(master, width=43, height=15, selectmode='single')

        def launch(database="recipes.csv"):  # looks for scraped recipe and retrieves best option
            file = open(database)
            recipes_df = pd.read_csv(file, header=[0])

            my_ingredients = listbox_overview.get(0, END)

            my_result = {}
            my_present = 0
            my_absent = 1000

            for index, row in recipes_df.iterrows():
                present = 0
                absent = 0

                for i in my_ingredients:

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

            y = 0
            for i in my_result:
                listbox_recipes.insert(y, i)
                y += 1

            return my_result

        def adding():  # allows user to add an ingredient to the list
            listbox_overview.insert(END, temp.get())
            entry_box_ingredient.delete(0, END)

        def clear_select():  # allows user to remove one ingredient
            listbox_overview.delete(0, END)
            listbox_recipes.delete(0, END)

        def clearing():  # allows user to clear all ingredients
            listbox_overview.delete(ANCHOR)

        def open_recipe():  # opens the selected recipe
            webbrowser.open("google.com", new=0, autoraise=True)

        # Buttons GUI
        button_add = Button(master, text="add ingredient", command=adding)
        button_access = Button(master, text="Search recipes", command=launch)
        button_clear = Button(master, text="remove all ingredients", command=clear_select)
        button_remove = Button(master, text="remove selected ingredient", command=clearing)
        button_open_recipe = Button(master, text="Open selected recipe", command=open_recipe, width=36)

        # Entry box GUI
        entry_box_ingredient = Entry(master, textvariable=temp, width=40)

        # Placement of elements on roster / canvas
        # Labels
        label_ingredient.place(x=10, y=130)
        label_overview.place(x=10, y=10)
        label_suggested.place(x=275, y=10)

        # Entry box
        entry_box_ingredient.place(x=10, y=305)

        # Buttons
        button_add.place(x=275, y=300)
        button_remove.place(x=380, y=300)
        button_clear.place(x=10, y=340)
        button_access.place(x=150, y=340)
        button_open_recipe.place(x=275, y=340)

        # List boxes
        listbox_overview.place(x=10, y=40)
        listbox_recipes.place(x=275, y=40)


# Run example
root = Tk()
temp = StringVar()
my_gui = Interface(root)
root.mainloop()

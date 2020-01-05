from bs4 import BeautifulSoup
import requests
import pandas as pd

all_titles = []
all_ingredients = []
all_instructions = []
all_links = []


#cooking the soup from page 2 - 166
for x in range(166):
    source = requests.get('https://kookidee.nl/recepten/page/'+str(x)+'/').text
    soup = BeautifulSoup(source, 'html.parser')

    #looks for the titles of recipes in the earlier retrieved soup, also finds the link
    for listbigbox in soup.find_all('article', class_='list big box1 recept'):
        rec_title = (listbigbox.h2.a.text)
        rec_link = (listbigbox.a['href'])

    #go into the actual recipe page and make a soup of it's data
        recipe_source = requests.get(rec_link).text
        recipe_soup = BeautifulSoup(recipe_source, 'html.parser')

    #finds all the html code that contains ingredients, make all the contents into a list.
        find_ingredients_html = recipe_soup.find_all('span', itemprop="recipeIngredient")
        list_of_ingredients = [x.text for x in find_ingredients_html]

     #finds the instructions for the recipe and converts it to text
        instructions_text_html = recipe_soup.find('div', itemprop="recipeInstructions")
        instruction_text = (instructions_text_html.text)

    all_titles.append(rec_title)
    all_ingredients.append(list_of_ingredients)
    all_instructions.append(instruction_text)
    all_links.append(rec_link)

    for listbigbox in soup.find_all('article', class_='list big box2 recept'):
        rec_title2 = listbigbox.h2.a.text
        rec_link2 = (listbigbox.a['href'])
    # go into the actual recipe page and make a soup of it's data
        recipe_source2 = requests.get(rec_link2).text
        recipe_soup2 = BeautifulSoup(recipe_source2, 'html.parser')
    # finds all the html code that contains ingredients, make all the contents into a list.
        find_ingredients_html2 = recipe_soup2.find_all('span', itemprop="recipeIngredient")
        list_of_ingredients2 = [x.text for x in find_ingredients_html2]

    # finds the instructions for the recipe and converts it to text
        instructions_text_html2 = recipe_soup2.find('div', itemprop="recipeInstructions")
        instruction_text2 = instructions_text_html2.text
    all_titles.append(rec_title2)
    all_ingredients.append(list_of_ingredients2)
    all_instructions.append(instruction_text2)
    all_links.append(rec_link2)

# create dataframe
final_array = []
for title, ingredients, instructions, link in zip(all_titles, list(all_ingredients), all_instructions, all_links):
    final_array.append({'recept': title, 'ingrediënten': ingredients, 'Instructions': instructions, 'url': link})

dataframe = pd.DataFrame(final_array)

print(dataframe)




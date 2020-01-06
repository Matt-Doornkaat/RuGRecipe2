import pip
import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import csv
page_number = 2
recipe_urls = []
recipe_title = []
ingredients = []
#print(str(page_number))
for x in range (0,100):
    index_url = "https://www.leukerecepten.nl/gerechten/hoofdgerechten/page/"+(str(page_number))+"/"
#print(index_url)
    recipe_index = r.get(index_url)
    recipe_index_data = BeautifulSoup(recipe_index.text, 'html.parser')
    recipe_options = recipe_index_data.find_all('div', {"class": "stream-card--list is-small"})
    for i in recipe_options:
        recipe_href = i.find("a").attrs["href"]
        recipe_urls.append(recipe_href)
    page_number += 1
    if page_number > 2: #a universal if break system would be nice here, in case the website expands
        break
#print(recipe_urls)

for url in recipe_urls:
    #Recipe Title
    recipe_data = r.get(url)
    recipe_soup = BeautifulSoup(recipe_data.text, 'html.parser')
    recipe_content = recipe_soup.find('div', {"class": "page-content"})
    recipe_header = recipe_content.find("h1").text
    recipe_header = recipe_header.strip("\n")
    recipe_title.append(recipe_header)

#Trouble shoot tests
    #print(url)

    #Ingredients
    recipe_ingredients = recipe_soup.find('ul', {"class": "page-content__ingredients-list"})
    recipe_ingredient_list = recipe_ingredients.find_all('li')
    list_ingedrients_individual_recipe =[]

    for ingredient in recipe_ingredient_list:
        ingredient_name = ingredient.find('label').text
        ingredient_name = ingredient_name.strip("\n")
        list_ingedrients_individual_recipe.append(ingredient_name)

    ingredients.append(list_ingedrients_individual_recipe)

recepten_lijst = pd.DataFrame(
    {'Titel van het Recept': recipe_title,
     'Ingredienten': ingredients,
     'Website URLS': recipe_urls
    })
recepten_lijst.to_csv("recepten.csv")
print(recepten_lijst)

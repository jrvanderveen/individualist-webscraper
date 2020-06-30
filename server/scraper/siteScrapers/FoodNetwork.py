from server.scraper import BeautifulSoup
import urllib.request as URLRequest
import re


class FoodNetwork(object):
    @staticmethod
    def getRecipeData(url):
        req = URLRequest.Request(url)
        html_content = URLRequest.urlopen(req).read()
        soup = BeautifulSoup(html_content, 'html.parser')
        ingredients = soup.findAll("p", {"class": "o-Ingredients__a-Ingredient"})
        name = soup.find("title").get_text().replace(" Recipe | Food Network Kitchen | Food Network", "")       
        data = {
                "ingredients": [],
                "name": name,
                }       
        for ingredient in ingredients:
            ingredientString = ingredient.get_text().strip("\n").strip().strip("\n")
            if ingredientString and ingredientString != "Add all ingredients to list":
                data["ingredients"].append(ingredientString)        
        return data
from server.scraper import BeautifulSoup
import urllib.request as URLRequest
import re


class AllRecipes(object):
	@staticmethod
	def getRecipeData(url):
		req = URLRequest.Request(url)
		html_content = URLRequest.urlopen(req).read()
		soup = BeautifulSoup(html_content, 'html.parser')
		ingredients = soup.findAll("span", {"class": "ingredients-item-name"})
		name = soup.find("title").get_text().replace(" | Allrecipes", "")

		data = {
				"ingredients": [],
				"name": name,
				}

		for ingredient in ingredients:
			ingredientString = ingredient.get_text().strip("\n").strip().strip("\n")
			if ingredientString and ingredientString != "Add all ingredients to list":
				data["ingredients"].append(ingredientString)


		return data
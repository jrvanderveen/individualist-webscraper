from server import app
from server import webScraper
from flask import request  # pylint: disable=import-error


@app.route("/api/v1/scraper/fullRecipe", methods=['POST'])
def getFullRecipe():
    res = webScraper.handleRequestForFullRecipe(request.get_json())
    return res


@app.route("/api/v1/scraper/recipe", methods=['POST'])
def getRecipe():
    res = webScraper.handleRequestForRecipe(request.get_json())
    return res


@app.route("/api/v1/scraper/recipe/ingredients", methods=['GET'])
def getRecipeIngredients():
    res = webScraper.handleRequestForIngredients(request.get_json())
    return res

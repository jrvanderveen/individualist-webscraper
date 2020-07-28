# from server.scraper.siteScrapers import AllRecipes, FoodNetwork
from server.scraper.siteScrapers import GeneralPurpose
import urllib.parse as parseURL

# Sites


class URLDispatcher:

    def handleRequestForFullRecipe(self, data):
        print(data)
        if "url" in data:
            urlParsedDict = parseURL.urlparse(data["url"])
            return self.dispatch(urlParsedDict)
        else:
            return {}

    def handleRequestForRecipe(self, data):
        print(data)
        if "url" in data:
            urlParsedDict = parseURL.urlparse(data["url"])
            recipe = self.dispatch(urlParsedDict)
            return {"URL": recipe["URL"], "name": recipe["name"], "servings": recipe["servings"], "ingredients": recipe["ingredients"]}
        else:
            return {}

    def handleRequestForIngredients(self, data):
        if "url" in data:
            urlParsedDict = parseURL.urlparse(data["url"])
            recipe = self.dispatch(urlParsedDict)
            return {"ingredients": recipe["ingredients"]}
        else:
            return {}

    def dispatch(self, urlParsedDict):
        fullURL = urlParsedDict.scheme + "://" + \
            urlParsedDict.netloc + urlParsedDict.path
        test = GeneralPurpose.getRecipeData(fullURL)
        return test

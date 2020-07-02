# from server.scraper.siteScrapers import AllRecipes, FoodNetwork
from server.scraper.siteScrapers import GeneralPurpose
import urllib.parse as parseURL

# Sites


class URLDispatcher:

    def handleRequestForRecipe(self, data):
        print(data)
        if "url" in data:
            urlParsedDict = parseURL.urlparse(data["url"])
            return self.dispatch(urlParsedDict)
        else:
            return {}

    def handleRequestForIngredients(self, data):
        if "url" in data:
            urlParsedDict = parseURL.urlparse(data["url"])
            recipeData = self.dispatch(urlParsedDict)
            return {"ingredients": recipeData["ingredients"]} if "ingredients" in recipeData else {"ingredients": []}
        else:
            return {"ingredients": []}

    def dispatch(self, urlParsedDict):
        fullURL = urlParsedDict.scheme + "://" + \
            urlParsedDict.netloc + urlParsedDict.path
        detailedRecipe = GeneralPurpose.getRecipeData(fullURL)

        # if urlParsedDict.netloc == 'www.allrecipes.com':
        #   fullURL= urlParsedDict.scheme + "://" + urlParsedDict.netloc + urlParsedDict.path
        #   detailedRecipe  = AllRecipes.getRecipeData(fullURL)

        # elif urlParsedDict.netloc == 'www.foodnetwork.com':
        #   fullURL= urlParsedDict.scheme + "://" + urlParsedDict.netloc + urlParsedDict.path
        #   detailedRecipe = FoodNetwork.getRecipeData(fullURL)

        return detailedRecipe

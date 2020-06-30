from server.scraper.siteScrapers.AllRecipes import AllRecipes
import urllib.parse as parseURL

# Sites


class URLDispatcher:
      
  def handleRequestForRecipe(self, data):
    if "url" in data:
      urlParsedDict = parseURL.urlparse(data["url"])
      return self.dispatch(urlParsedDict)
    else:
      return {}

  def handleRequestForIngredients(self, data):
    if "url" in data:
      urlParsedDict = parseURL.urlparse(data["url"])
      recipeData = self.dispatch(urlParsedDict)
      return {"ingredients" : recipeData["ingredients"]} if "ingredients" in recipeData else {"ingredients": []}
    else:
      return {"ingredients": []}

  def dispatch(self, urlParsedDict):
    if urlParsedDict.netloc == 'www.allrecipes.com':
      fullURL= urlParsedDict.scheme + "://" + urlParsedDict.netloc + urlParsedDict.path
      detailedRecipe  = AllRecipes.getRecipeData(fullURL)
      return detailedRecipe
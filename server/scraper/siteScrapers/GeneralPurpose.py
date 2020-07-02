from recipe_scrapers import scrape_me


class GeneralPurpose(object):
    @staticmethod
    def getRecipeData(url):
        # give the url as a string, it can be url from any site listed below
        try:

            scraper = scrape_me(url)
            if(scraper.title() == "" or scraper.ingredients() == []):
                return dict({"error": "Recipe not found"})
            return dict({"name": scraper.title(),
                         "servings": int(scraper.yields()) if scraper.yields().isnumeric() else 1,
                         "URL": url,
                         "ingredients": scraper.ingredients(),
                         })
        # scrape_me can return recipe not implemented error
        except Exception as e:
            return dict({"error": str(e)})

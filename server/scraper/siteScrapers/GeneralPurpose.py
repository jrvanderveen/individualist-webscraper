from recipe_scrapers import scrape_me

class GeneralPurpose(object):
    @staticmethod
    def getRecipeData(url):

        # give the url as a string, it can be url from any site listed below
        try:
            scraper = scrape_me(url)
            return dict({"name": scraper.title(), "ingredients":scraper.ingredients()})
        # scrape_me can return recipe not implemented error
        except Exception as e:
                return dict({"error": e})
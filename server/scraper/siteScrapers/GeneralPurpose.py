from recipe_scrapers import scrape_me


class GeneralPurpose(object):
    @staticmethod
    def getRecipeData(url):
        # give the url as a string, it can be url from any site listed below
        try:
            scraper = scrape_me(url)
            recipe = dict()
            recipe["name"] = scraper.title()
            recipe["total_time"] = scraper.total_time()
            yields = ''.join(c for c in scraper.yields() if c.isdigit())
            recipe["servings"] = int(
                yields) if yields.isdigit() else scraper.yields()
            recipe["ingredients"] = scraper.ingredients()
            recipe["instructions"] = scraper.instructions()
            recipe["image"] = scraper.image()
            recipe["URL"] = url
            if(scraper.title() == "" or scraper.ingredients() == []):
                return dict({"error": "Recipe not found"})
            return recipe
        # scrape_me can return recipe not implemented error
        except Exception as e:
            return dict({"error": str(e)})

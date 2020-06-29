from server import app
from server import webScraperApp


@app.route("/api/v1/ingredients", methods=['GET'])
def home():
    # webScraperApp.handleRequest(request)
    return ["ingredient one", "ingredient two"]

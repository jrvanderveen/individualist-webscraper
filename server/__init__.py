from flask import Flask
app = Flask(__name__)
from server.scraper import webScraper
webScraperApp = webScraper
from server import routes


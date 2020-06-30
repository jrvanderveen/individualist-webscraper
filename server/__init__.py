from flask import Flask # pylint: disable=import-error
app = Flask(__name__)
from server.scraper import webScraper
from server import routes


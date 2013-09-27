
from __future__ import absolute_import
import requests
from bs4 import BeautifulSoup

class eBaseScrapper(object):
    """ BaseClass for scrapping """
    def __init__(self, urlbase):
        self.urlbase = urlbase
        self.s = None

    def loadpage(self):
        """" Load the page, and process on BS4  """
        ## Request page
        ## TODO: Raise error if not load ok
        page = requests.get(self.url)
        ## Process the HTML DOM
        self.s = BeautifulSoup(page.text)
        return self

from __future__ import absolute_import
import requests
from bs4 import BeautifulSoup

class eBaseScrapper(object):
    """ BaseClass for scrapping """
    def __init__(self, urlbase, **params):
        self.urlbase = urlbase
        self.url = None
        self.s = None
        self.params = params or {}


    def setURL(self, page=None):
        self.url = "{url}/{page}".format(url=self.urlbase,
                                        page=page or '')
        return self

    def loadpage(self):
        """" Load the page, and process on BS4  """
        ## Request page
        ## TODO: Raise error if not load ok
        ## TODO: .get() can receive parameters
        page = requests.get(self.url,params = self.params)
        ## Process the HTML DOM
        self.s = BeautifulSoup(page.text)

        return self
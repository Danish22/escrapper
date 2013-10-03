
"""
Base classes and import statements
"""
from __future__ import absolute_import
import requests
from bs4 import BeautifulSoup

class _BaseScrapper(object):
    """ BaseClass for scrapping """
    def __init__(self, urlbase, **params):
        self.urlbase = urlbase
        self.url = None
        self.soup = None
        self.params = params or {}


    def seturl(self, page=None):
        """" set URL to processes with Requests.get() """
        self.url = "{url}/{page}".format(url=self.urlbase,
                                        page=page or '')
        return self

    def loadpage(self):
        """" Load the page, and process on BS4  """
        ## Request page
        ## TODO: Raise error if not load ok
        page = requests.get(self.url, params = self.params)
        ## Process the HTML DOM
        self.soup = BeautifulSoup(page.text)

        return self

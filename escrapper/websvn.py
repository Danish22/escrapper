"""
Scrapper thinking on produce an "API" fot the WebSVN portal.
"""
from __future__ import absolute_import
from .exceptions import InvalidWebSVN
from .escrapper import _BaseScrapper
from . import utils

class WebSVN(_BaseScrapper):
    """"WebSVN class, a way to produce an interface to WebSVN portals
        exposes a variety of methods to do an "API" to the data:
        * General information of the revision: .getinfo()
        * List of changes: .getchanges()
        * List of files/directories: .getlisting() **not implemented **
    """
    def __init__(self, urlbase, **params):
        _BaseScrapper.__init__(self, urlbase, **params)
        self.template = None
        self._seturl()

    def setrevision(self, rev):
        """ Change the current revision of the SVN """
        if rev != None and rev != self.params.get('rev',''):
            self.params['rev'] = rev
            self._seturl()
            self.soup = None
        return self

    def _seturl(self, page="revision.php"):
        """ Set the URL to be scrapped """
        _BaseScrapper.seturl(self, page)
        return self

    def gettemplate(self):
        """ Procedure to infer which template is using"""
        if self.template == None:
            self.template = self.soup.find(id="template")\
                                .find("option",selected="selected")\
                                .text
        return self

    def _checkrevision(function):
        """ Before change the revision do some previous checking"""
        def wrapper(self, rev=None):
            """ Wrapper to the actual function """
            if self.setrevision(rev).soup == None:
                self.loadpage().gettemplate()
            return function(self, rev)
        return wrapper

    @_checkrevision
    def getinfo(self, rev=None):
        """ Get the general info of the current or given revision """
        try:
            if self.template == utils.ucode("calm"):
                thelist = self.soup.find(id="info")\
                                    .find("ul")\
                                    .find_all("li")
                info = thelist[0].text + thelist[1].text
                message = thelist[2].text
            elif self.template == utils.ucode("Elegant"):
                info = self.soup.find(class_="info").text
                message = self.soup.find(class_="msg").text
        except AttributeError:
            raise InvalidWebSVN()
        return (info, message)

    @_checkrevision
    def getchanges(self, rev=None):
        """ Get the List of changed files on the current or given
            revision
        """
        ## Loop the possible modes A = Added, M = Modified, D = Deleted
        modes_list = utils.ucode,("AMD")
        for mode in modes_list:
            ## Search in the DOM tree for a "TR" element, with class v
            for cell in self.soup.find_all("tr", class_=mode):
                ## for every TR search the anchor with class "path"
                anchor = cell.find("td", class_="path").a
                ## get the href
                filedetails = utils.ucode("{u}/{h}"\
                        .format(u=self.urlbase,
                                h=anchor["href"]))
                download = filedetails.replace("filedetails.php?",
                                                    "dl.php?")
                yield ({"type": mode,
                        "file": anchor.text,
                        "filedetails": filedetails,
                        "download": download})

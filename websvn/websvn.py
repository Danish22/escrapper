import requests
from bs4 import BeautifulSoup

class WebSVNs(object):
    def __init__(self, urlbase, reponame, path="/", rev="HEAD"):
        self.urlbase = urlbase
        self.reponame = reponame
        self.path = path
        self.rev = rev
        self.s = None
        ## Set URL
        self.setURL()

    def setRevision(self,rev):
        self.rev = rev
        return self

    def setURL(self,action="revision.php"):
        self.url = "{url}/{a}?{r}&path=/{p}/&rev={rev}"\
            .format(url=self.urlbase, a=action,
                    r=self.reponame, p=self.path, rev=self.rev)
        return self

    def loadpage(self):
        ## Request page
        page = requests.get(self.url)
        ## Process the HTML DOM
        self.s = BeautifulSoup(page.text)
        return self

    def getInfo(self,rev=None):
        if rev != self.rev :
            self.setRevision(rev).setURL().loadpage()
        if self.s == None:
            self.loadpage()
        info = self.s.find(class_="info").text
        message = self.s.find(class_="msg").text
        return (info,message)

    def getChanges(self,rev=None):
        if rev != self.rev :
            self.setRevision(rev).setURL().loadpage()
        if self.s == None:
            self.loadpage()
        ## The possible modes D = Deleted , "A" = Added, "M" = Modified
        modes = (u"D",u"A",u"M")
        for v in modes:
            ## Search in the DOM tree for a "TR" element, with class v
            for tr in self.s.find_all("tr", class_=v):
                ## for every TR search the anchor with class "path"
                a = tr.find("td", class_="path").a
                ## get the href
                href = u"{u}/{h}"\
                        .format(u=self.urlbase,
                                h=a["href"].replace("filedetails.php?",
                                                    "dl.php?"))
                yield ({"type": v, "file": a.text, "href": href})
from __future__ import absolute_import
from .exceptions import InvalidWebSVN
from .escrapper import eBaseScrapper

class WebSVN(eBaseScrapper):
    def __init__(self, urlbase, reponame, path="/", rev="HEAD"):
        eBaseScrapper.__init__(self,urlbase)
        self.reponame = reponame
        self.path = path
        self.rev = rev
        self.template = None
        self.setURL()

    def setRevision(self,rev):
        if rev != None and rev != self.rev :
            self.rev = rev
            self.setURL()
            self.s = None
        return self

    def setURL(self,action="revision.php"):
        self.url = "{url}/{a}?{r}&path=/{p}/&rev={rev}"\
            .format(url=self.urlbase, a=action,
                    r=self.reponame, p=self.path, rev=self.rev)
        return self

    def getTemplate(self):
        """ Procedure to infer which template is using"""
        if self.template == None:
            self.template = self.s.find(id="template")\
                               .find("option",selected="selected")\
                               .text
        return self

    def checkRevision(fn):
        def wrapper(self,rev=None):
            if self.setRevision(rev).s == None:
                self.loadpage().getTemplate()
            return fn(self,rev)
        return wrapper

    @checkRevision
    def getInfo(self,rev=None):
        try:
            if self.template==u"calm":
                ul = self.s.find(id="info").find("ul").find_all("li")
                info = ul[0].text + ul[1].text
                message = ul[2].text
            elif self.template==u"Elegant":
                info = self.s.find(class_="info").text
                message = self.s.find(class_="msg").text
        except AttributeError:
            raise InvalidWebSVN()
        return (info,message)

    @checkRevision
    def getChanges(self,rev=None):
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
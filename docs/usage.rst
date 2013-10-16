========
Usage
========

To use eScrapper in a project::
        ## Load the WebSVN module 
	from escrapper import WebSVN
        ## WebSVN class with defaults, revision = HEAD
        W = WebSVN("http://websvn.meneame.net")
        ## Get the general info of the current revision
        print(W.getinfo())
        ## Show the changes on HEAD revision
        for changes in W.getchanges():
           print(changes)



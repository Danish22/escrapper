========
Usage
========

To use eScrapper in a project::

	from escrapper import WebSVN
        W = WebSVN("http://websvn.meneame.net")
        W.getinfo()
        ## Show the changes on HEAD revision
        for changes in W.getchanges()
           print(changes)



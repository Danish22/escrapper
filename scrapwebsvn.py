from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import os
import sys

urlbase = "http://websvn.meneame.net"
action = "revision.php"
repo = "meneame"
path = "branches/version4"
rev = 3770

url = "{url}/{a}?{r}&path=/{p}/&rev={rev}" \
    .format(url=urlbase, a=action, r=repo, p=path, rev=rev)
print("Downloading page")
page = requests.get(url)
print("Done. File Size {l}".format(l=len(page.text)))
## Process the HTML
s = BeautifulSoup(page.text)
## THe possible modes
m = {"D": "Deleted", "A": "Added", "M": "Modified"}
#m = {"D":"Deleted"}
for k, v in m.items():
    print("Searching for {v}".format(v=v))
    ## Search in the DOM tree for a "TR" element, with class k
    for tr in s.find_all("tr", class_=k):
        ## for every TR search the anchor with class "path"
        a = tr.find("td", class_="path").a
        ## get the href
        href = a["href"].replace("filedetails.php?", "dl.php?")
        ## get the file we're gonna work on
        thefile = a.text.replace("/{p}/".format(p=path), "")
        print("Archive to {v}:\t\nfile={f} \t\nurl={url}"
               .format(v=v, f=thefile, url=href))
        if k == "D":
            if not os.path.exists(thefile):
                msg = "ERROR: file {f} not found!\n".format(f=thefile)
                sys.stderr.write(msg)
            else:
                os.remove(thefile)
        else:
            with open(thefile,"w") as f:
                print("Downloading new file {f} from {h}"\
                       .format(f=thefile, h=href))
                newfile = requests.get("{url}/{h}"\
                                    .format(url=urlbase, h=href))
                print(newfile.text)
                f.write(newfile.text)

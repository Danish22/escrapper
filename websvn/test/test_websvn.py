from websvn import WebSVNs

## Test URLs
urls = {"elegant": ("http://websvn.meneame.net","meneame"),
        "calm": ("http://demo.websvn.info","WebSVN")}
Objs = {}

for k,v in urls.items():
   Objs[k] = WebSVNs(v[0],v[1])

def test_created():
    """ Test if we can create the objects  """
    for o in Objs.itervalues():
        assert isinstance(o,WebSVNs)

def test_getinfo():
    """ Test if we can getinfo of the current revision """
    for o in Objs.itervalues():
        r = o.getInfo()
        assert type(r) == tuple

def test_setRevision():
    """ Test if we can set the revision """
    assert Objs["elegant"].setRevision(3138).rev == 3138

def test_setURL():
    """ Test if we change the URL correctly """
    assert Objs["elegant"].setURL().url == urls["elegant"][0]\
                    +"/revision.php?meneame&path=///&rev=3138"
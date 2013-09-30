from escrapper import WebSVN

## Test URLs
urls = {"elegant": ("http://websvn.meneame.net",
                    {'repname':"meneame",
                     'rev': 3138}),
        "calm": ("http://demo.websvn.info",
                 {'repname':"WebSVN"})}
Objs = {}

for k,v in urls.items():
   Objs[k] = WebSVN(v[0],**v[1])

def test_created():
    """ Test if we can create the objects  """
    for o in Objs.itervalues():
        assert isinstance(o,WebSVN)

def test_getinfo():
    """ Test if we can getinfo of the current revision """
    for o in Objs.itervalues():
        r = o.getInfo()
        assert type(r) == tuple

def test_getChanges():
    """ Test if we can get the Changes of the current revision"""
    for o in Objs.itervalues():
        r = o.getChanges()
        ## is an iterable? in this case it should be a generator
        assert hasattr(r,'__iter__')

def test_setRevision():
    """ Test if we can set the revision """
    assert Objs["elegant"].setRevision(3150).params['rev'] == 3150

def test_setURL():
    """ Test if we change the URL correctly """
    assert Objs["elegant"].setURL().url == urls["elegant"][0]\
                                            +"/revision.php"
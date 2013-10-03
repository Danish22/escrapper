""" Test suit for escrapper package """

from escrapper import WebSVN

## Test URLs
urls = {"elegant": ("http://websvn.meneame.net",
                    {'repname':"meneame",
                     'rev': 3138}),
        "calm": ("http://demo.websvn.info",
                 {'repname':"WebSVN"})}
Objs = {}

for k, v in urls.items():
    Objs[k] = WebSVN(v[0], **v[1])

def test_created():
    """ Test if we can create the objects  """
    for test_object in Objs.values():
        assert isinstance(test_object, WebSVN)

def test_getinfo():
    """ Test if we can getinfo of the current revision """
    for test_object in Objs.values():
        assert isinstance(test_object.getinfo(), tuple)

def test_getchanges():
    """ Test if we can get the Changes of the current revision"""
    for test_object in Objs.values():
        ## is an iterable? in this case it should be a generator
        assert hasattr(test_object.getchanges(), '__iter__')

def test_setrevision():
    """ Test if we can set the revision """
    assert Objs["elegant"].setrevision(3150).params['rev'] == 3150



""" Test suit for escrapper package """

from escrapper import WebSVN, InvalidWebSVN
import pytest

## Test URLs
URLS = {"elegant": ("http://websvn.meneame.net",
                    {'repname': "meneame",
                     'rev': 3138}),
        "calm": ("http://demo.websvn.info",
                 {'repname': "WebSVN"})}
OBJS = {}

for k, v in URLS.items():
    OBJS[k] = WebSVN(v[0], **v[1])


def test_created():
    """ Test if we can create the objects """
    for test_object in OBJS.values():
        assert isinstance(test_object, WebSVN)


def test_getinfo():
    """ Test if we can getinfo of the current revision """
    for test_object in OBJS.values():
        assert isinstance(test_object.getinfo(), tuple)


def test_getchanges():
    """ Test if we can get the Changes of the current revision"""
    for test_object in OBJS.values():
        ## is an iterable? in this case it should be a generator
        changes = test_object.getchanges()
        assert hasattr(next(changes), '__iter__')


def test_setrevision():
    """ Test if we can set the revision """
    assert OBJS["elegant"].setrevision(3150).params['rev'] == 3150


def test_invalidwebsvn():
    """ Test if we have an error with a no-WebSVN site """
    with pytest.raises(InvalidWebSVN):
        websvn_test = WebSVN("http://google.com")
        websvn_test.getinfo()

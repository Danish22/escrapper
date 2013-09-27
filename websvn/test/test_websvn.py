from websvn import WebSVNs

W = WebSVNs("http://websvn.meneame.net","meneame")

def test_created():
    assert isinstance(W,WebSVNs)

def test_getinfo():
    r,_ = W.getInfo()
    assert r.split("\n")[0] == u'Rev 3771'

def test_getinfo_with_parameters():
    r,_ = W.getInfo(3770)
    assert r.split("\n")[0] == u'Rev 3770'

def test_setRevision():
    assert W.setRevision(3138).rev == 3138

def test_setURL():
    assert W.setURL().url == "http://websvn.meneame.net/revision.php?meneame&path=///&rev=3138"
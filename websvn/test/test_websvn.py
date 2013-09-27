from websvn import WebSVNs

urlbase = "http://meneame.net"
W = WebSVNs(urlbase,"meneame")

def test_created():
    assert isinstance(W,WebSVNs)

def test_getinfo():
    ## Can call getInfo() without parameters (means HEAD),
    ## Of course, that will not be a good test
    r,_ = W.getInfo(3771)
    assert r.split("\n")[0] == u'Rev 3771'

def test_setRevision():
    assert W.setRevision(3138).rev == 3138

def test_setURL():
    assert W.setURL().url == urlbase+"/revision.php?meneame&path=///&rev=3138"
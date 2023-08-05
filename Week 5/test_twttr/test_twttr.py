from twttr import shorten


def test_shorten():
    assert shorten("name") == "nm"
    assert shorten("KIWI") == "KW"
    assert shorten("BlackMamba123") == "BlckMmb123"
    assert shorten("rtfds") == "rtfds"
    assert shorten("LouisXIV") == "LsXV"
    assert shorten("sa,lut") == "s,lt" 

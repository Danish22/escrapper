"""
Utility functions, some of them to dealing with py2K & py3K
"""
import sys
if sys.version < '3':
    import codecs

    def ucode(_string):
        """Returns the unicode object from a str object
           On Py3K return the string (it's unicode by default)
        """
        return codecs.unicode_escape_decode(_string)[0]
else:
    def ucode(_string):
        """Returns the unicode object from a str object
           On Py3K return the string (it's unicode by default)
        """
        return _string


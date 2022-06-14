"""
StrongHelp page parser.
"""

import stronghelp.format


class StrongHelpPage(object):

    def __init__(self, sh, filename=None, content=None, encoding=None):
        self.sh = sh
        self.title = None
        self.filename = filename
        self.shfile = None
        if content is None:
            self.shfile = self.sh[filename]
            content = self.shfile.read(encoding=encoding)
        self.content = content

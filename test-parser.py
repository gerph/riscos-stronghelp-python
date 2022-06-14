"""
Manual testing for the parser
"""

import stronghelp.format
import stronghelp.parser

sh = stronghelp.format.StrongHelp('SH-RefMan,3d6')

shpage = stronghelp.parser.StrongHelpPage(sh, '$.psyntax')

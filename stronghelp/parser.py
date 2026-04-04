"""
StrongHelp page parser.
"""

import stronghelp.format

commands = []

class SHCommandError(Exception):
    pass


def register_command(cls):
    commands.append(command)
    return cls


class SHCommandBase(object):
    name = "<unknown>"
    match = "NEVER"

    def __init__(self, args):
        pass

    def __repr__(self):
        return "<{}()>".format(self.__class__.__name__)


@register_command
class SHCommandAlign(SHCommandBase):
    """
    Align: Where on a line to place the text
    """
    name = "Align"
    match = "Align(?: |$)"

    # Values the align property holds for the positions or 'unstack'
    values = {
            'left': -1,
            'centre': 0,
            'right': 1,
            '': None,
        }

    def __init__(self, args):
        super(SHCommandAlign, self).__init__(args)
        args = args.lower()
        try:
            self.align = self.values[args]
        except KeyError:
            raise SHCommandError("Invalid 'align' arguments: {}".format(args))


@register_command
class SHCommandBackground(SHCommandBase):
    """
    Background: How the page background should appear
    """
    name = "Background"
    match = "Background(?: |$)"

    def __init__(self, args):
        super(SHCommandBackground, self).__init__(args)
        # Syntax: Background \{ Wimp no | RGB no,no,no | Tile spritename }
        # FIXME: N/I


@register_command
class SHCommandBelow(SHCommandBase):
    """
    Below: Continue next line below all graphics
    """
    name = "Below"
    match = "Below(?: |$)"

    def __init__(self, args):
        super(SHCommandBelow, self).__init__(args)
        # No arguments.

@register_command
class SHCommandBottom(SHCommandBase):
    """
    Bottom: Move everything below to the bottom of the page
    """
    name = "Bottom"
    match = "Bottom(?: |$)"

    def __init__(self, args):
        super(SHCommandBottom, self).__init__(args)
        # No arguments.


@register_command
class SHCommandDraw(SHCommandBase):
    """
    Draw: Place a drawfile on the page
    """
    name = "Draw"
    match = "Draw(?: |$)"

    def __init__(self, args):
        super(SHCommandDraw, self).__init__(args)
        # Syntax: Draw x,y drawfilename
        # FIXME: N/I


@register_command
class SHCommandEndtable(SHCommandBase):
    """
    Endtable: Table>   End of a #Table
    """
    name = "Endtable"
    match = "Endtable(?: |$)"

    def __init__(self, args):
        super(SHCommandEndtable, self).__init__(args)
        # No arguments.


@register_command
class SHCommandF(SHCommandBase):
    """
    F: Define/Set physical or logical font.
    """
    name = "F"
    match = "F(?: |$)"

    def __init__(self, args):
        super(SHCommandF, self).__init__(args)
        # Syntax: <many>
        # FIXME: N/I


@register_command
class SHCommandInclude(SHCommandBase):
    """
    Include: Include a source file
    """
    name = "Include"
    match = "Include(?: |$)"

    def __init__(self, args):
        super(SHCommandInclude, self).__init__(args)
        # Syntax: #Include fname
        # FIXME: N/I


@register_command
class SHCommandIndent(SHCommandBase):
    """
    Indent: Set indent to be used by the following text
    """
    name = "Indent"
    match = "Indent(?: |$)"

    def __init__(self, args):
        super(SHCommandIndent, self).__init__(args)
        # Syntax: #Indent [[+]number]
        # FIXME: N/I


@register_command
class SHCommandLine(SHCommandBase):
    """
    Line: Place a horizontal line on the page
    """
    name = "Line"
    match = "Line(?: |$)"

    def __init__(self, args):
        super(SHCommandLine, self).__init__(args)
        # Syntax: #Line
        # FIXME: N/I


@register_command
class SHCommandManuals(SHCommandBase):
    """
    Manuals: Expands to a list of all installed manuals
    """
    name = "Manuals"
    match = "Manuals(?: |$)"

    def __init__(self, args):
        super(SHCommandManuals, self).__init__(args)
        # Syntax: #Manuals
        # FIXME: N/I


@register_command
class SHCommandParent(SHCommandBase):
    """
    Parent: Defines parent for a page without history
    """
    name = "Parent"
    match = "Parent(?: |$)"

    def __init__(self, args):
        super(SHCommandParent, self).__init__(args)
        # Syntax: #parent name
        # FIXME: N/I

@register_command
class SHCommandPrefix(SHCommandBase):
    """
    Prefix: Prefixed to \<link> to get complete link
    """
    name = "Prefix"
    match = "Prefix(?: |$)"

    def __init__(self, args):
        super(SHCommandPrefix, self).__init__(args)
        # Syntax: #Prefix string
        # FIXME: N/I


@register_command
class SHCommandPostfix(SHCommandBase):
    """
    Postfix: Prefix>   Postfixed to \<link> to get complete link
    """
    name = "Postfix"
    match = "Postfix(?: |$)"

    def __init__(self, args):
        super(SHCommandPostfix, self).__init__(args)
        # Syntax: #Postfix string
        # FIXME: N/I


@register_command
class SHCommandRGB(SHCommandBase):
    """
    RGB: Set colour to be used on the following text
    """
    name = "RGB"
    match = "RGB(?: |$)"

    def __init__(self, args):
        super(SHCommandRGB, self).__init__(args)
        # Syntax: #RGB red,green,blue
        # FIXME: N/I


@register_command
class SHCommandSprite(SHCommandBase):
    """
    Sprite: Place a sprite on the page
    """
    name = "Sprite"
    match = "Sprite(?: |$)"

    def __init__(self, args):
        super(SHCommandSprite, self).__init__(args)
        # Syntax: #Sprite x,y name [label] [=>link]
        # FIXME: N/I


@register_command
class SHCommandSpritefile(SHCommandBase):
    """
    Spritefile: Defines where to find a #Sprite
    """
    name = "Spritefile"
    match = "Spritefile(?: |$)"

    def __init__(self, args):
        super(SHCommandSpritefile, self).__init__(args)
        # Syntax: #SpriteFile name
        # FIXME: N/I


@register_command
class SHCommandSubpage(SHCommandBase):
    """
    Subpage: Announces end of current page, and beginning of a subpage
    """
    name = "Subpage"
    match = "Subpage(?: |$)"

    def __init__(self, args):
        super(SHCommandSubpage, self).__init__(args)
        # Syntax: #Subpage name
        # FIXME: N/I


@register_command
class SHCommandTab(SHCommandBase):
    """
    Tab: Starts/Ends section formatted with the TAB character
    """
    name = "Tab"
    match = "Tab(?: |$)"

    def __init__(self, args):
        super(SHCommandTab, self).__init__(args)
        # Syntax: #Tab { "," [format] }
        # FIXME: N/I


@register_command
class SHCommandTable(SHCommandBase):
    """
    Table: Order the following lines in columns
    """
    name = "Table"
    match = "Table(?: |$)"

    def __init__(self, args):
        super(SHCommandTable, self).__init__(args)
        # Syntax: #Table [Columns | Lines] no
        # FIXME: N/I


@register_command
class SHCommandTag(SHCommandBase):
    """
    Tag: Defines a tag that a link can refer.
    """
    name = "Tag"
    match = "Tag(?: |$)"

    def __init__(self, args):
        super(SHCommandTag, self).__init__(args)
        # Syntax: #TAG tag
        # FIXME: N/I


@register_command
class SHCommandWrap(SHCommandBase):
    """
    Wrap: Tells StrongHelp how to preprocess the lines
    """
    name = "Wrap"
    match = "Wrap(?: |$)"

    def __init__(self, args):
        super(SHCommandWrap, self).__init__(args)
        # Syntax: #Wrap [ On | Off | Nojoin ]
        # FIXME: N/I


class StrongHelpCommandParser(object):
    """
    Parser for the commands we know about.
    """
    def __init__(self):
        self.commands = list((cls, re.compile(cls.match)) for cls in commands)

    def parse(self, command):
        command.

class StrongHelpParser(object):

    def __init__(self, shpage):
        self.sh = shpage.sh
        self.shpage = shpage
        self.title = None

        self.blocks = []

        for line in self.shpage.content.splitlines():
            if not self.title:
                self.title = line

            if line.startswith('#'):
                # This is a command, which doesn't introduce a new paragraph
                if line.startswith('# ') or line == '#':
                    # These are just comments, so they're ignored
                    continue
                self.process_commands(line)
                continue

            else:
                self.process_line(line)

    def process_line(self, line):
        """
        Process a line of input.
        """
        # FIXME
        pass

    def process_commands(self, line):
        """
        Process commands in a line. They may be separated by a ';' character.
        """
        parts = line.split(';')
        for part in parts:
            # Trim leading and trailing whitespace, as these are ignored.
            part = part.strip()
            # 
        pass


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

        parser = StrongHelpParser(self)
        self.title = parser.title
        self.blocks = parser.blocks

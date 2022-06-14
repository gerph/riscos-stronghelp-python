# Python StrongHelp reader

This repository contains a reader for the RISC OS StrongHelp manual image format.

The Python module is able to be used to parse the format and return the files which are
present. The module can also be used as a command line tool to extract the files to a
unix file system.

## Command line

At the command line the extraction tool may be used with the
supplied shell commamnd:

    riscos-shextract --extract-dir <directory> <stronghelp-file>

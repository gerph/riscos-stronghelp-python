#!/usr/bin/env python
"""
Command line tool for extracting StrongHelp manuals into a directory.

    python -m riscos_stronghelp --extract-dir <directory> <stronghelp-file>
    python -m riscos_stronghelp --list <stronghelp-file>
"""

from __future__ import print_function
import argparse
import os
import sys

from riscos_stronghelp.format import StrongHelp, objtype_dir

RISCOS_FILETYPES = {
    0xFFF: 'Text',
    0xFFE: 'Command',
    0xFFD: 'Data',
    0xFFC: 'Utility',
    0xFFB: 'BASIC',
    0xFFA: 'Module',
    0xFF9: 'Sprite',
    0xFF8: 'Absolute',
    0xFF7: 'BBC font',
    0xFF6: 'Font',
    0xFF5: 'PoScript',
    0xFF4: 'Printout',
    0xFF2: 'Config',
    0xFF0: 'TIFF',
    0xFD1: 'BasicTxt',
    0xFED: 'Palette',
    0xFEC: 'Template',
    0xFEB: 'Obey',
    0xFEA: 'Desktop',
    0xFE6: 'Unix Ex',
    0xFE5: 'EPROM',
    0xFDC: 'SoftLink',
    0xFD3: 'DebImage',
    0xFCA: 'Squash',
    0xFC9: 'SunRastr',
    0xFAF: 'HTML',
    0xFAE: 'Resource',
    0xF89: 'GZip',
    0xF81: 'JS',
    0xF80: 'XML',
    0xF7F: 'XML_DTD',
    0xF7E: 'XSL',
    0xF75: 'JSON',
    0xF74: 'YAML',
    0xD94: 'ArtWork',
    0xC85: 'JPEG',
    0xBBC: 'BBC ROM',
    0xB61: 'XBM',
    0xB60: 'PNG',
    0xB2F: 'WMF',
    0xAFF: 'DrawFile',
    0xAAD: 'SVG',
    0xA91: 'Zip',
    0xA66: 'WebP',
    0xA65: 'JPEG2000',
    0x69E: 'PNM',
    0x69D: 'Targa',
    0x69C: 'BMP',
    0x697: 'PCX',
    0x695: 'GIF',
    0x690: 'Clear',
    0x1C9: 'DiagData',
    0x132: 'ICO',
    0x1000: 'Directory',
}


def extract_to_directory(sh, output_dir):
    """
    Extract the whole archive to a target directory.
    """
    try:
        os.makedirs(output_dir)
    except OSError:
        pass

    for shf in sh:
        print("Extracting {}".format(shf.filename))
        filename = os.path.join(output_dir, shf.unix_filename)
        if shf.objtype == objtype_dir:
            try:
                os.makedirs(filename)
            except OSError:
                pass
        else:
            with open(filename, 'wb') as fh:
                fh.write(shf.read())


def list_files(sh):
    """
    List files in the StrongHelp archive.
    """
    print("{:<25} {:<12} {:>10}".format("Name", "Type", "Length"))
    print("-" * 50)
    for shf in sh:
        if shf.objtype == objtype_dir:
            type_str = "Directory"
        elif shf.filetype == -1:
            type_str = "None"
        else:
            type_str = RISCOS_FILETYPES.get(shf.filetype, "{:03x}".format(shf.filetype))

        print("{:<25} {:<12} {:10d}".format(shf.filename, type_str, shf.length))


def setup_argparse():
    parser = argparse.ArgumentParser(usage="%s [<options>] <strong-help-file>" % (os.path.basename(sys.argv[0]),))
    parser.add_argument('file', action='store',
                        help="StrongHelp file to read")
    parser.add_argument('--extract-dir', action='store',
                        help="Directory to extract into")
    parser.add_argument('--list', action='store_true',
                        help="List files in the StrongHelp file")

    return parser


def main():
    parser = setup_argparse()

    options = parser.parse_args()

    sh = StrongHelp(options.file)

    if options.list:
        list_files(sh)
    elif options.extract_dir:
        extract_to_directory(sh, options.extract_dir)
    else:
        # Default behavior if no action specified: list files
        list_files(sh)


if __name__ == '__main__':
    main()

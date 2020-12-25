"""
__main__.py
Collen Roller
collen.roller@gmail.com

Creates the CLI application for Flydenity
"""

import sys
from flydenity import Parser


def main():
    """Main of CLI app"""

    parser = Parser()
    print({arg: parser.parse(arg) for arg in sys.argv[1:]})


if __name__ == "__main__":
    main()

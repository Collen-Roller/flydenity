"""
__main__.py
Collen Roller
collen.roller@gmail.com

Creates the CLI application for Flydenity
"""

import sys
import json

def main():
    """Main of CLI app
    """
    from flydenity import parser

    parser = parser.ARParser()
    for tail in sys.argv[1:]:
        #print("%s: %s" % (tail,parser.parse(tail)))
        print({tail:parser.parse(tail)})

if __name__ == "__main__":
    main()

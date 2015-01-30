#
# This file is part of Neubot <https://www.neubot.org/>.
#
# Neubot is free software. See AUTHORS and LICENSE for more
# information on the copying conditions.
#

""" HTTP main """

import getopt
import logging
import sys

from .serve import serve

USAGE = """\
usage: python -m neubot_http [-m async] [-v] [-d rootdir]
       python -m neubot_http -m forked [-v] [-d rootdir]
       python -m neubot_http -m threaded [-v] [-d rootdir]
       python -m neubot_http -m single [-v] [-d rootdir]"""

def main():
    """ Main function """

    settings = {}
    level = logging.WARNING

    try:
        options, arguments = getopt.getopt(sys.argv[1:], "d:m:v")
    except getopt.error:
        sys.exit(USAGE)
    if arguments:
        sys.exit(USAGE)

    for name, value in options:
        if name == "-d":
            settings["rootdir"] = value
        elif name == "-m":
            settings["mode"] = value
        elif name == "-v":
            level = logging.DEBUG
        else:
            sys.exit(USAGE)

    logging.basicConfig(level=level, format="%(message)s")

    serve(settings)

if __name__ == "__main__":
    main()

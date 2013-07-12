"""
``monoseq`` command line interface.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE file.
"""


import sys
import argparse

from .monoseq import pprint_sequence


def pprint(sequence):
    """
    Pretty-print sequence.
    """
    pass


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('sequence', metavar='SEQUENCE', help='sequence')

    args = parser.parse_args()
    pprint(args.sequence)


if __name__ == '__main__':
    main()

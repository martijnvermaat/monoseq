"""
monoseq: pretty-printing sequence strings command line interface.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE file.
"""


import sys
import argparse

from .monoseq import pprint_sequence


def pprint(sequence_file, annotation=None):
    """
    Pretty-print sequence.
    """
    annotation = annotation or []

    sequence = sequence_file.read().strip()
    annotations = [[(first - 1, last) for first, last in annotation]]

    print pprint_sequence(sequence, annotations=annotations, mode='ansi')


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(
        description='monoseq: pretty-printing sequence strings')
    parser.add_argument('sequence_file', metavar='FILENAME', nargs='?',
                        default=sys.stdin, type=argparse.FileType('r'),
                        help='file to read sequence from (default: standard '
                        'input)')
    parser.add_argument('-a', metavar='POS', dest='annotation', nargs=2,
                        action='append', type=int, help='first and last '
                        'positions of subsequence to annotate (allowed more '
                        'than once)')

    args = parser.parse_args()
    pprint(args.sequence_file, annotation=args.annotation)


if __name__ == '__main__':
    main()

"""
monoseq: pretty-printing sequence strings command line interface.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE.rst file.
"""


from __future__ import print_function

import argparse
import itertools
import sys

from .monoseq import AnsiFormat, pprint_sequence


def _until_eof(stream):
    """
    Yield lines from an open file.

    Iterating over `sys.stdin` continues after EOF marker. This is annoying,
    since it means having to type ``^D`` twice to stop. Wrap this function
    around the stream to stop at the first EOF marker.
    """
    while True:
        line = stream.readline()
        if line == '':
            break
        yield line


def _fasta_iter(fasta):
    """
    Given an open FASTA file, yield tuples of (`header`, `sequence`).
    """
    # Adapted from Brent Pedersen.
    # http://www.biostars.org/p/710/#1412
    groups = (group for _, group in
              itertools.groupby(fasta, lambda line: line.startswith('>')))
    for group in groups:
        header = next(group)[1:].strip()
        sequence = ''.join(line.strip() for line in next(groups))
        yield header, sequence


def _pprint_fasta(fasta, annotations=None, block_length=10,
                  blocks_per_line=6):
    """
    Pretty-print each record in the FASTA file.
    """
    annotations = annotations or []
    for header, sequence in _fasta_iter(fasta):
        print(header)
        print(pprint_sequence(sequence, annotations=annotations,
                              block_length=block_length,
                              blocks_per_line=blocks_per_line,
                              format=AnsiFormat))


def _pprint_line(line, annotations=None, block_length=10, blocks_per_line=6):
    """
    Pretty-print one line.
    """
    annotations = annotations or []
    print(pprint_sequence(line, annotations=annotations,
                          block_length=block_length,
                          blocks_per_line=blocks_per_line, format=AnsiFormat))


def pprint(sequence_file, annotation=None, block_length=10,
           blocks_per_line=6):
    """
    Pretty-print sequence(s) from a file.
    """
    annotations = [[(first - 1, last) for first, last in annotation or []]]

    try:
        # Peek to see if this looks like a FASTA file.
        line = next(sequence_file)
        if line.startswith('>'):
            _pprint_fasta(itertools.chain([line], sequence_file),
                          annotations=annotations, block_length=block_length,
                          blocks_per_line=blocks_per_line)
        else:
            _pprint_line(line.strip(), annotations=annotations,
                         block_length=block_length,
                         blocks_per_line=blocks_per_line)
    except StopIteration:
        pass


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(
        description='monoseq: pretty-print sequence strings')
    parser.add_argument('sequence_file', metavar='FILENAME', nargs='?',
                        default=sys.stdin, type=argparse.FileType('r'),
                        help='file to read sequence(s) from, can be in FASTA '
                        'format (default: standard input)')
    parser.add_argument('-b', metavar='INT', dest='block_length', type=int,
                        default=10, help='block length (default: 10)')
    parser.add_argument('-l', metavar='INT', dest='blocks_per_line', type=int,
                        default=6, help='blocks per line (default: 6)')
    parser.add_argument('-a', metavar='POS', dest='annotation', nargs=2,
                        action='append', type=int, help='first and last '
                        'positions of subsequence to annotate (allowed more '
                        'than once)')

    args = parser.parse_args()
    pprint(_until_eof(args.sequence_file), annotation=args.annotation,
           block_length=args.block_length,
           blocks_per_line=args.blocks_per_line)


if __name__ == '__main__':
    main()

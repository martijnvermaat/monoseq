"""
Command line interface to ``monoseq``.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE.rst file.
"""


from __future__ import print_function

import argparse
import collections
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


def _bed_iter(bed):
    """
    Given an open BED file, yield tuples of (`chrom`, `chrom_iter`) where
    `chrom_iter` yields tuples of (`start`, `stop`).
    """
    records = (line.split()[:3] for line in bed if
               not (line.startswith('browser') or line.startswith('track')))

    for chrom, chrom_iter in itertools.groupby(records, lambda x: x[0]):
        yield chrom, ((int(start), int(stop))
                      for _, start, stop in chrom_iter)


def _pprint_fasta(fasta, annotations=None, annotation_file=None,
                  block_length=10, blocks_per_line=6):
    """
    Pretty-print each record in the FASTA file.
    """
    annotations = annotations or []

    # Annotations by chromosome.
    as_by_chrom = collections.defaultdict(lambda: [a for a in annotations] or [])
    if annotation_file:
        for chrom, chrom_iter in _bed_iter(annotation_file):
            as_by_chrom[chrom].append(list(chrom_iter))

    for header, sequence in _fasta_iter(fasta):
        print(header)
        print(pprint_sequence(sequence,
                              annotations=as_by_chrom[header.split()[0]],
                              block_length=block_length,
                              blocks_per_line=blocks_per_line,
                              format=AnsiFormat))


def _pprint_line(line, annotations=None, annotation_file=None,
                 block_length=10, blocks_per_line=6):
    """
    Pretty-print one line.
    """
    annotations = annotations or []

    if annotation_file:
        # We just use the first chromosome defined in the BED file.
        _, chrom_iter = next(_bed_iter(annotation_file))
        annotations.append(list(chrom_iter))

    print(pprint_sequence(line, annotations=annotations,
                          block_length=block_length,
                          blocks_per_line=blocks_per_line, format=AnsiFormat))


def pprint(sequence_file, annotation=None, annotation_file=None,
           block_length=10, blocks_per_line=6):
    """
    Pretty-print sequence(s) from a file.
    """
    annotations = []

    if annotation:
        annotations.append([(first - 1, last) for first, last in annotation])

    try:
        # Peek to see if this looks like a FASTA file.
        line = next(sequence_file)
        if line.startswith('>'):
            _pprint_fasta(itertools.chain([line], sequence_file),
                          annotations=annotations,
                          annotation_file=annotation_file,
                          block_length=block_length,
                          blocks_per_line=blocks_per_line)
        else:
            _pprint_line(line.strip(), annotations=annotations,
                         annotation_file=annotation_file,
                         block_length=block_length,
                         blocks_per_line=blocks_per_line)
    except StopIteration:
        pass


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(
        description='monoseq: pretty-printing DNA and protein sequences',
        epilog='If INPUT is in FASTA format, each record is pretty-printed '
        'after printing its name and ANNOTATION (if supplied) is used by '
        'matching chromosome/record name. If INPUT contains a raw sequence, '
        'only the first chromosome in ANNOTATION is used.')
    parser.add_argument(
        'sequence_file', metavar='INPUT', nargs='?', default=sys.stdin,
        type=argparse.FileType('r'), help='file to read sequence(s) from, '
        'can be in FASTA format (default: standard input)')
    parser.add_argument(
        '-b', '--block-length', metavar='LENGTH', dest='block_length',
        type=int, default=10, help='block length in letters (default: 10)')
    parser.add_argument(
        '-l', '--blocks-per-line', metavar='BLOCKS', dest='blocks_per_line',
        type=int, default=6, help='blocks per line (default: 6)')
    parser.add_argument(
        '-a', '--annotation', metavar='POS', dest='annotation', nargs=2,
        action='append', type=int, help='first and last positions of '
        'subsequence to annotate (allowed more than once)')
    parser.add_argument(
        '-e', '--bed', metavar='ANNOTATION', dest='annotation_file',
        type=argparse.FileType('r'), help='file to read annotation from in '
        'BED format')

    args = parser.parse_args()
    pprint(_until_eof(args.sequence_file), annotation=args.annotation,
           annotation_file=args.annotation_file,
           block_length=args.block_length,
           blocks_per_line=args.blocks_per_line)


if __name__ == '__main__':
    main()

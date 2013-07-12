"""
``monoseq``, a Python library for pretty-printing sequence strings using a
monospace font.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE file.
"""


import math
from itertools import chain


def partition_range(stop, annotations=None):
    """
    Partition the range from 0 to `stop` based on annotations.

    :arg stop: End point (not included) of the range (similar to the `stop`
        argument of the built-in `range` function).
    :type stop: int
    :arg annotations: For each annotation level, a list of (`start`, `stop`)
        pairs defining an annotated region.
    :type annotations: list

    :return: Partitioning of the range as (`start`, `stop`, `levels`) tuples
        defining a region with a set of annotation levels.
    :rtype: list

    All regions (`start`, `stop`) are defined as in slicing notation, so
    zero-based and `stop` is not included.

    The `annotations` argument is a list of annotations. An annotation is a
    list of regions as (`start`, `stop`) tuples. The level of each annotation
    is its index in `annotations`.

        >>> partition_range(50, annotations=[[(0, 21), (30, 35)],
        ...                                  [(15, 32), (40, 46)]])
        [(0, 15, {0}),
         (15, 21, {0, 1}),
         (21, 30, {1}),
         (30, 32, {0, 1}),
         (32, 35, {0}),
         (35, 40, set()),
         (40, 46, {1}),
         (46, 50, set())]

    Annotation regions can overlap (overlap within one level is ignored) and
    do not need to be sorted.
    """
    annotations = annotations or []

    partitioning = []
    part_start, part_levels = 0, None

    # We loop over the range, only touching positions where levels potentially
    # change.
    for p in sorted(set(chain([0, stop], *chain(*annotations)))):
        if p == stop:
            partitioning.append( (part_start, p, part_levels) )
            break

        # Annotation levels for position p.
        levels = {level for level, regions in enumerate(annotations)
                  if any(x <= p < y for x, y in regions)}

        if p == 0:
            part_levels = levels
            continue

        if levels != part_levels:
            partitioning.append( (part_start, p, part_levels) )
            part_start, part_levels = p, levels

    return partitioning


def pprint_sequence(sequence, annotations=None, block_length=10,
                    blocks_per_line=6, mode='html'):
    """
    Pretty-print sequence for use with a monospace font.

    :arg sequence: Sequence to pretty-print.
    :type sequence: str or any sliceable yielding slices representable as
        strings.
    :arg annotations: For each annotation level, a list of (`start`, `stop`)
        pairs defining an annotated region.
    :type annotations: list
    :arg block_length: Length of space-separated blocks.
    :type block_length: int
    :arg blocks_per_line: Number of blocks per line.
    :type blocks_per_line: int
    :arg mode: Mode to use for formatting styles. Must be one of ``html``,
        ``ansi``, ``plaintext``.
    :type mode: str

    :return: Pretty-printed version of `sequence`.
    :rtype: str

    All regions (`start`, `stop`) are defined as in slicing notation, so
    zero-based and `stop` is not included.

    The `annotations` argument is a list of annotations. An annotation is a
    list of regions as (`start`, `stop`) tuples. The level of each annotation
    is its index in `annotations`.

        >>> sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
        >>> print pprint_sequence(sequence, mode='plaintext')
          1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS
         61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI
        121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH
        181  ICWIKIFKAF GT

    Annotation regions can overlap (overlap within one level is ignored) and
    do not need to be sorted.

    The number of annotation levels supported depends on `mode`. For ``html``,
    10 levels are supported and for ``ansi``, 3 levels are supported. Any
    additional annotations are ignored. Annotations are ignored completely if
    `mode`=``plaintext``.
    """
    annotations = annotations or []

    if mode == 'html':
        delimiters = [('<span class="level%i-annotation">' % i, '</span>')
                      for i in range(5)]
    elif mode == 'ansi':
        delimiters = [('\033[91m', '\033[0m'), # Red.
                      ('\033[1m', '\033[0m'),  # Bold.
                      ('\033[4m', '\033[0m')]  # Underline.
    elif mode == 'plaintext':
        delimiters = []
    else:
        raise ValueError('invalid mode: ' + repr(mode))

    partitioning = partition_range(len(sequence), annotations)

    # The maximum length for positions is the 10_log of the length of the
    # sequence.
    margin = int(math.floor(math.log(max(len(sequence), 1), 10)) + 1)
    result = '1'.rjust(margin) + ' '

    for p in range(0, len(sequence), block_length):
        # Partitioning of the block starting at position p.
        block = [(max(start, p), min(stop, p + block_length), levels)
                 for start, stop, levels in partitioning
                 if start < p + block_length and stop > p]

        result += ' '
        for start, stop, levels in block:
            d = [(left, right) for level, (left, right)
                 in enumerate(delimiters) if level in levels]
            result += (''.join(left for left, right in reversed(d)) +
                       sequence[start:stop] +
                       ''.join(right for left, right in d))

        if (not (p + block_length) % (block_length * blocks_per_line) and
            p + block_length < len(sequence)):
            result += '\n' + str(p + block_length + 1).rjust(margin) + ' '

    return result

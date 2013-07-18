Command line interface
======================

Simple pretty-printing of sequences on the command line is done with the
``monoseq`` command. It reads one or more sequences from a file or from
standard input and pretty-prints them to standard output. The input can be a
raw sequence, or any number of sequences in FASTA format.

Example::

    martijn@hue:~$ S=MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT
    martijn@hue:~$ echo $S$S$S$S | monoseq
      1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS
     61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI
    121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH
    181  ICWIKIFKAF GT


Formatting options
------------------

The number of letters per block can be specified with the ``-b`` argument and
the ``-l`` argument sets the number of blocks per line.


Annotations
-----------

Subsequences can be specified for annotation with the ``-a`` argument followed
by the first and the last position of the subsequence, both one-based. For
example, to annotate the first 10 bases and the 17th base, you would add ``-a
1 10 -a 17 17``.

In addition, annotation is read from the BED track specified with the ``-e``
argument. If the input is a raw sequence, only the first chromosome is used
from the BED track. If the input is a FASTA file, chromosomes are matched with
record names.


More information
----------------

Use the ``--help`` argument for more information.
